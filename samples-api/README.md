# Exemplo de API RESTful com FastAPI

Este exemplo demonstra a **facilidade de criar uma API** usando FastAPI e Uvicorn.

## 📋 Pré-requisitos

Certifique-se de ter o ambiente `py12api` criado e ativado:

```bash
conda activate py12api
```

Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

**OU** instale os pacotes essenciais manualmente:

```bash
pip install fastapi uvicorn pytz
```

## 🚀 Como Executar

### Opção 1: Usando Uvicorn diretamente

```bash
uvicorn main:app --reload
```

### Opção 2: Executando o arquivo Python

```bash
python main.py
```

A API estará disponível em: **http://localhost:8000**

## 📚 Documentação Interativa

FastAPI gera automaticamente documentação interativa:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔗 Endpoints Disponíveis

### 1. Informações da API
```
GET /
```
Retorna informações sobre a API e seus endpoints.

**Exemplo de resposta:**
```json
{
  "message": "API de Data e Hora",
  "endpoints": {
    "/datetime": "Retorna data/hora atual em UTC",
    "/datetime/{timezone}": "Retorna data/hora em um timezone específico"
  }
}
```

### 2. Data/Hora em UTC
```
GET /datetime
GET /datetime?timezone={timezone}
```
Retorna a data e hora atual em UTC, ou em um timezone específico usando query parameter.

**Exemplo de resposta (UTC):**
```json
{
  "timezone": "UTC",
  "datetime": "2025-12-16T14:30:00+00:00",
  "timestamp": 1734357000.0,
  "formatted": "2025-12-16 14:30:00 UTC"
}
```

### 3. Data/Hora em Timezone Específico
```
GET /datetime/tz/{timezone}
```
Retorna a data e hora em um timezone específico usando path parameter.

**Exemplos de uso (Path Parameter):**

```bash
# Horário de São Paulo
curl http://localhost:8000/datetime/tz/America/Sao_Paulo

# Horário de Nova York
curl http://localhost:8000/datetime/tz/America/New_York

# Horário de Londres
curl http://localhost:8000/datetime/tz/Europe/London

# Horário de Tóquio
curl http://localhost:8000/datetime/tz/Asia/Tokyo
```

**Alternativa usando Query Parameter:**

```bash
# Horário de São Paulo
curl "http://localhost:8000/datetime?timezone=America/Sao_Paulo"

# Horário de Nova York
curl "http://localhost:8000/datetime?timezone=America/New_York"

# Horário de Londres
curl "http://localhost:8000/datetime?timezone=Europe/London"
```

**Exemplo de resposta:**
```json
{
  "timezone": "America/Sao_Paulo",
  "datetime": "2025-12-16T11:30:00-03:00",
  "timestamp": 1734357000.0,
  "formatted": "2025-12-16 11:30:00 -03",
  "offset": "-0300"
}
```

### 4. Listar Timezones Comuns
```
GET /timezones
```
Retorna uma lista de timezones comuns organizados por região.

## 🧪 Testando a API

### Usando o navegador
Abra: http://localhost:8000/datetime

### Usando curl
```bash
# UTC
curl http://localhost:8000/datetime

# São Paulo (Path Parameter)
curl http://localhost:8000/datetime/tz/America/Sao_Paulo

# São Paulo (Query Parameter)
curl "http://localhost:8000/datetime?timezone=America/Sao_Paulo"

# Nova York
curl http://localhost:8000/datetime/tz/America/New_York

# Lista de timezones
curl http://localhost:8000/timezones
```

### Usando Python
```python
import requests

# UTC
response = requests.get("http://localhost:8000/datetime")
print(response.json())

# Timezone específico (Path Parameter)
response = requests.get("http://localhost:8000/datetime/tz/America/Sao_Paulo")
print(response.json())

# Timezone específico (Query Parameter)
response = requests.get("http://localhost:8000/datetime", params={"timezone": "America/Sao_Paulo"})
print(response.json())
```
