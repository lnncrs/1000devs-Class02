# API de Inferência com Machine Learning

Este exemplo demonstra a **facilidade de criar uma API de Machine Learning** usando FastAPI, Uvicorn e scikit-learn.

## 📋 Pré-requisitos

Certifique-se de ter o ambiente `py12ai` criado e ativado:

```bash
conda activate py12ai
```

Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

**OU** instale os pacotes essenciais manualmente:

```bash
pip install fastapi uvicorn scikit-learn pandas numpy
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
**GET** `/`

Retorna informações gerais sobre a API e endpoints disponíveis.

**Resposta:**
```json
{
  "message": "API de Inferência - Classificação de Câncer de Mama",
  "model": "best_classification_model.pkl",
  "endpoints": {
    "/": "Informações sobre a API",
    "/predict": "Realiza predição (POST)",
    "/health": "Verifica status da API e do modelo",
    "/features": "Lista as features esperadas pelo modelo"
  }
}
```

### 2. Realizar Predição
**POST** `/predict`

Realiza a predição usando o modelo treinado.

**Body (JSON):**
```json
{
  "features": [17.99, 10.38, 122.8, 1001.0, 0.1184, 0.2776, 0.3001, 0.1471, 0.2419, 0.07871]
}
```

**Resposta:**
```json
{
  "prediction": "M",
  "prediction_label": "Maligno",
  "probability": {
    "B": 0.05,
    "M": 0.95
  },
  "confidence": 0.95
}
```

### 3. Verificar Saúde da API
**GET** `/health`

Verifica se a API e o modelo estão funcionando corretamente.

**Resposta:**
```json
{
  "status": "healthy",
  "model_loaded": true,
  "model_path": "../outputs/best_classification_model.pkl"
}
```

### 4. Listar Features
**GET** `/features`

Retorna a lista de features (características) esperadas pelo modelo.

**Resposta:**
```json
{
  "num_features": 10,
  "feature_names": [
    "radius", "texture", "perimeter", "area",
    "smoothness", "compactness", "concavity",
    "concave_points", "symmetry", "fractal_dimension"
  ],
  "description": "Features do Wisconsin Diagnostic Breast Cancer dataset"
}
```

## 📊 Sobre o Modelo

O modelo carregado foi treinado com o **Wisconsin Diagnostic Breast Cancer (WDBC) dataset** e classifica tumores como:

- **M (Maligno)**: Tumor cancerígeno
- **B (Benigno)**: Tumor não-cancerígeno

### Features do Modelo

O modelo espera 10 características numéricas calculadas a partir de imagens de células:

1. **radius** - Raio médio
2. **texture** - Textura
3. **perimeter** - Perímetro
4. **area** - Área
5. **smoothness** - Suavidade
6. **compactness** - Compacidade
7. **concavity** - Concavidade
8. **concave_points** - Pontos côncavos
9. **symmetry** - Simetria
10. **fractal_dimension** - Dimensão fractal

## 🧪 Exemplo de Uso com cURL

```bash
# Fazer uma predição
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "features": [17.99, 10.38, 122.8, 1001.0, 0.1184, 0.2776, 0.3001, 0.1471, 0.2419, 0.07871]
  }'
```

## 🧪 Exemplo de Uso com Python

```python
import requests

# Dados para predição
data = {
    "features": [
        17.99,  # radius
        10.38,  # texture
        122.8,  # perimeter
        1001.0, # area
        0.1184, # smoothness
        0.2776, # compactness
        0.3001, # concavity
        0.1471, # concave_points
        0.2419, # symmetry
        0.07871 # fractal_dimension
    ]
}

# Fazer a requisição
response = requests.post("http://localhost:8000/predict", json=data)
result = response.json()

print(f"Predição: {result['prediction_label']}")
print(f"Confiança: {result['confidence']:.2%}")
```

## 📝 Notas

- O modelo é carregado automaticamente ao iniciar a API
- Se o modelo não for encontrado, a API retornará erro 503 (Service Unavailable)
- As predições incluem probabilidades para ambas as classes (B e M)
- A API valida se o número de features está correto (deve ser 10)
- O modelo foi treinado usando apenas as features "mean" do dataset original
