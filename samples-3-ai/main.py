"""
API de Inferência - Machine Learning
Demonstra como servir um modelo de ML usando FastAPI e Uvicorn
"""

import os
import pickle
from pathlib import Path
from typing import List

import joblib
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# Caminho para o modelo
MODEL_PATH = Path(__file__).parent.parent / "outputs" / "best_classification_model.pkl"

# Inicializar FastAPI
app = FastAPI(
    title="API de Inferência - Classificação de Câncer de Mama",
    description="API para realizar predições usando modelo treinado de classificação",
    version="1.0.0",
)

# Variável global para armazenar o modelo
model = None

# Feature names do Wisconsin Diagnostic Breast Cancer dataset
# O modelo foi treinado com apenas 10 features (mean values)
FEATURE_NAMES = [
    "radius",
    "texture",
    "perimeter",
    "area",
    "smoothness",
    "compactness",
    "concavity",
    "concave_points",
    "symmetry",
    "fractal_dimension",
]


class PredictionInput(BaseModel):
    """Schema para entrada de predição"""

    features: List[float] = Field(
        ...,
        description="Lista com 10 características numéricas do tumor",
        min_length=10,
        max_length=10,
    )

    class Config:
        json_schema_extra = {
            "example": {
                "features": [
                    17.99,  # radius
                    10.38,  # texture
                    122.8,  # perimeter
                    1001.0,  # area
                    0.1184,  # smoothness
                    0.2776,  # compactness
                    0.3001,  # concavity
                    0.1471,  # concave_points
                    0.2419,  # symmetry
                    0.07871,  # fractal_dimension
                ]
            }
        }


class PredictionOutput(BaseModel):
    """Schema para saída de predição"""

    prediction: str = Field(..., description="Classe predita (M=Maligno, B=Benigno)")
    prediction_label: str = Field(..., description="Label da predição em português")
    probability: dict = Field(..., description="Probabilidades para cada classe")
    confidence: float = Field(
        ..., description="Confiança da predição (probabilidade da classe predita)"
    )


@app.on_event("startup")
async def load_model():
    """Carrega o modelo ao iniciar a API"""
    global model
    try:
        if not MODEL_PATH.exists():
            print(f"⚠️  AVISO: Modelo não encontrado em {MODEL_PATH}")
            print(
                "   A API será iniciada, mas as predições não funcionarão até que o modelo esteja disponível."
            )
            return

        print(f"📂 Tentando carregar modelo de: {MODEL_PATH}")

        # Tentar carregar com joblib (mais comum para scikit-learn)
        try:
            model = joblib.load(MODEL_PATH)
            print(f"✅ Modelo carregado com sucesso usando joblib")
        except:
            # Se falhar, tentar com pickle
            print("⚠️  Falha com joblib, tentando pickle...")
            with open(MODEL_PATH, "rb") as f:
                model = pickle.load(f)
            print(f"✅ Modelo carregado com sucesso usando pickle")

        print(f"📊 Tipo do modelo: {type(model).__name__}")
        if hasattr(model, "classes_"):
            print(f"🏷️  Classes: {model.classes_}")

    except Exception as e:
        print(f"❌ Erro ao carregar modelo: {e}")
        import traceback

        traceback.print_exc()


@app.get("/")
def read_root():
    """
    Endpoint raiz - Informações sobre a API
    """
    return {
        "message": "API de Inferência - Classificação de Câncer de Mama",
        "model": "best_classification_model.pkl",
        "endpoints": {
            "/": "Informações sobre a API",
            "/predict": "Realiza predição (POST)",
            "/health": "Verifica status da API e do modelo",
            "/features": "Lista as features esperadas pelo modelo",
        },
        "examples": [
            "POST http://localhost:8000/predict",
            "GET http://localhost:8000/health",
            "GET http://localhost:8000/features",
        ],
    }


@app.get("/health")
def health_check():
    """
    Verifica se a API e o modelo estão funcionando
    """
    return {
        "status": "healthy" if model is not None else "model not loaded",
        "model_loaded": model is not None,
        "model_path": str(MODEL_PATH),
        "model_exists": MODEL_PATH.exists(),
    }


@app.get("/features")
def get_features():
    """
    Retorna a lista de features esperadas pelo modelo
    """
    return {
        "num_features": len(FEATURE_NAMES),
        "feature_names": FEATURE_NAMES,
        "description": "Features do Wisconsin Diagnostic Breast Cancer dataset",
        "note": "As features devem ser fornecidas nesta ordem no array 'features'",
    }


@app.post("/predict", response_model=PredictionOutput)
def predict(input_data: PredictionInput):
    """
    Realiza predição usando o modelo carregado

    Args:
        input_data: Dados de entrada contendo as 30 features

    Returns:
        PredictionOutput: Resultado da predição com probabilidades
    """
    # Verificar se o modelo está carregado
    if model is None:
        raise HTTPException(
            status_code=503,
            detail={
                "error": "Modelo não disponível",
                "message": f"O modelo não foi encontrado em {MODEL_PATH}",
                "suggestion": "Certifique-se de que o modelo foi treinado e salvo no diretório outputs/",
            },
        )

    try:
        # Converter features para array numpy
        features_array = np.array(input_data.features).reshape(1, -1)

        # Realizar predição
        prediction = model.predict(features_array)[0]
        probabilities = model.predict_proba(features_array)[0]

        # Obter classes do modelo
        classes = model.classes_

        # Criar dicionário de probabilidades
        prob_dict = {str(cls): float(prob) for cls, prob in zip(classes, probabilities)}

        # Determinar label da predição
        prediction_label = "Maligno" if prediction == "M" else "Benigno"

        # Confiança é a probabilidade da classe predita
        confidence = float(probabilities[np.where(classes == prediction)[0][0]])

        return PredictionOutput(
            prediction=str(prediction),
            prediction_label=prediction_label,
            probability=prob_dict,
            confidence=confidence,
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "error": "Erro ao realizar predição",
                "message": str(e),
                "suggestion": "Verifique se as features estão no formato correto",
            },
        )


if __name__ == "__main__":
    import uvicorn

    print("🚀 Iniciando API de Inferência...")
    print(f"📦 Modelo: {MODEL_PATH}")
    print(f"🌐 Acesse: http://localhost:8000")
    print(f"📚 Docs: http://localhost:8000/docs")

    uvicorn.run(app, host="0.0.0.0", port=8000)
