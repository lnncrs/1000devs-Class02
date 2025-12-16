"""
API de exemplo - Data e Hora
Demonstra a facilidade de criar uma API RESTful com FastAPI e Uvicorn
"""

from datetime import datetime

import pytz
from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="API de Data e Hora",
    description="API simples para retornar data/hora em diferentes timezones",
    version="1.0.0",
)


@app.get("/")
def read_root():
    """
    Endpoint raiz - Informações sobre a API
    """
    return {
        "message": "API de Data e Hora",
        "endpoints": {
            "/datetime": "Retorna data/hora atual em UTC",
            "/datetime/tz/{timezone}": "Retorna data/hora em um timezone específico (ex: /datetime/tz/America/Sao_Paulo)",
            "/datetime?timezone=America/Sao_Paulo": "Alternativa usando query parameter",
        },
        "exemplos": [
            "http://localhost:8000/datetime",
            "http://localhost:8000/datetime/tz/America/Sao_Paulo",
            "http://localhost:8000/datetime?timezone=Europe/London",
        ],
    }


@app.get("/datetime")
def get_datetime_utc(timezone: str = None):
    """
    Retorna a data e hora atual em UTC ou em um timezone específico

    Args:
        timezone (str, optional): Nome do timezone como query parameter (ex: ?timezone=America/Sao_Paulo)

    Returns:
        dict: Data/hora no timezone solicitado ou UTC se não especificado
    """
    # Se timezone for fornecido via query parameter
    if timezone:
        try:
            tz = pytz.timezone(timezone)
            now = datetime.now(tz)
            return {
                "timezone": timezone,
                "datetime": now.isoformat(),
                "timestamp": now.timestamp(),
                "formatted": now.strftime("%Y-%m-%d %H:%M:%S %Z"),
                "offset": now.strftime("%z"),
            }
        except pytz.exceptions.UnknownTimeZoneError:
            raise HTTPException(
                status_code=400,
                detail={
                    "error": f"Timezone '{timezone}' não encontrado",
                    "message": "Use um timezone válido da base de dados IANA",
                    "examples": [
                        "America/Sao_Paulo",
                        "America/New_York",
                        "Europe/London",
                        "Asia/Tokyo",
                    ],
                },
            )

    # Retorna UTC se nenhum timezone for especificado
    now_utc = datetime.now(pytz.UTC)
    return {
        "timezone": "UTC",
        "datetime": now_utc.isoformat(),
        "timestamp": now_utc.timestamp(),
        "formatted": now_utc.strftime("%Y-%m-%d %H:%M:%S %Z"),
    }


@app.get("/datetime/tz/{timezone:path}")
def get_datetime_timezone(timezone: str):
    """
    Retorna a data e hora atual em um timezone específico

    Args:
        timezone (str): Nome do timezone com caminho completo (ex: America/Sao_Paulo, America/New_York, Europe/London)

    Returns:
        dict: Data/hora no timezone solicitado
    """
    try:
        # Tenta obter o timezone
        tz = pytz.timezone(timezone)
        now = datetime.now(tz)

        return {
            "timezone": timezone,
            "datetime": now.isoformat(),
            "timestamp": now.timestamp(),
            "formatted": now.strftime("%Y-%m-%d %H:%M:%S %Z"),
            "offset": now.strftime("%z"),
        }
    except pytz.exceptions.UnknownTimeZoneError:
        # Lista alguns timezones comuns para ajudar o usuário
        common_timezones = [
            "America/Sao_Paulo",
            "America/New_York",
            "America/Chicago",
            "America/Los_Angeles",
            "Europe/London",
            "Europe/Paris",
            "Asia/Tokyo",
            "Australia/Sydney",
            "UTC",
        ]
        raise HTTPException(
            status_code=400,
            detail={
                "error": f"Timezone '{timezone}' não encontrado",
                "message": "Use um timezone válido da base de dados IANA",
                "examples": common_timezones,
                "help": "Veja a lista completa em: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones",
            },
        )


@app.get("/timezones")
def list_common_timezones():
    """
    Lista alguns timezones comuns disponíveis

    Returns:
        dict: Lista de timezones comuns por região
    """
    return {
        "americas": [
            "America/Sao_Paulo",
            "America/New_York",
            "America/Chicago",
            "America/Denver",
            "America/Los_Angeles",
            "America/Mexico_City",
            "America/Toronto",
        ],
        "europe": [
            "Europe/London",
            "Europe/Paris",
            "Europe/Berlin",
            "Europe/Madrid",
            "Europe/Rome",
            "Europe/Moscow",
        ],
        "asia": [
            "Asia/Tokyo",
            "Asia/Shanghai",
            "Asia/Singapore",
            "Asia/Dubai",
            "Asia/Kolkata",
        ],
        "oceania": ["Australia/Sydney", "Australia/Melbourne", "Pacific/Auckland"],
        "total_available": len(pytz.all_timezones),
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
