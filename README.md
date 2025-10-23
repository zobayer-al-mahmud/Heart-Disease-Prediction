Live Link : https://heart-disease-prediction-w1cq.onrender.com/docs
# Heart Disease Prediction API 🫀

A production-ready FastAPI application for predicting heart disease using Machine Learning (Random Forest Classifier).

## 📋 Features

- **FastAPI** REST API with automatic interactive documentation
- **Machine Learning** prediction using Random Forest (100% accuracy on test data)
- **Docker** containerization for easy deployment
- **Render-ready** deployment configuration included
- **Health checks** for monitoring
- **Pydantic** validation for request/response schemas

## 🏗️ Project Structure

```
heart-fastapi-docker/
├── app/
│   ├── __init__.py
│   ├── schemas.py       # Pydantic models
│   └── main.py          # FastAPI application
├── data/
│   └── heart.csv        # Training dataset
├── model/
│   ├── heart_model.joblib      # Trained model
│   ├── scaler.joblib           # Feature scaler
│   └── feature_names.joblib    # Feature names
├── train.py             # Model training script
├── requirements.txt     # Python dependencies
├── Dockerfile           # Multi-stage Docker build
├── docker-compose.yml   # Local development
├── render.yaml          # Render deployment config
└── README.md
```

## 🚀 Quick Start

### Option 1: Docker Compose (Recommended)

```bash
# Build and run
docker-compose build
docker-compose up

# Access the API
# Swagger UI: http://localhost:8000/docs
# ReDoc: http://localhost:8000/redoc
```

### Option 2: Local Development

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Train the model (if needed)
python train.py

# Run the API
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Option 3: Docker Only

```bash
# Build image
docker build -t heart-disease-api .

# Run container
docker run -p 8000:8000 heart-disease-api
```

## 📡 API Endpoints

### 1. Health Check
```http
GET /health
```
**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

### 2. Model Information
```http
GET /info
```
**Response:**
```json
{
  "model_type": "Random Forest Classifier",
  "version": "1.0.0",
  "features": ["age", "sex", "cp", ...],
  "accuracy": 1.0
}
```

### 3. Predict Heart Disease
```http
POST /predict
Content-Type: application/json
```
**Request Body:**
```json
{
  "age": 63,
  "sex": 1,
  "cp": 3,
  "trestbps": 145,
  "chol": 233,
  "fbs": 1,
  "restecg": 0,
  "thalach": 150,
  "exang": 0,
  "oldpeak": 2.3,
  "slope": 0,
  "ca": 0,
  "thal": 1
}
```
**Response:**
```json
{
  "heart_disease": true,
  "probability": 0.85,
  "risk_level": "high"
}
```

## 🌐 Deploy to Render

### Method 1: Using render.yaml (Recommended)

1. Push your code to GitHub
2. Go to [Render Dashboard](https://dashboard.render.com/)
3. Click "New +" → "Blueprint"
4. Connect your GitHub repository
5. Render will automatically detect `render.yaml` and deploy

### Method 2: Manual Setup

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name:** heart-disease-api
   - **Environment:** Docker
   - **Plan:** Free
   - **Health Check Path:** /health
5. Click "Create Web Service"

### Environment Variables (Optional)

```env
PORT=8000
PYTHONUNBUFFERED=1
```

## 🧪 Testing the API

### Using cURL

```bash
# Health check
curl http://localhost:8000/health

# Get model info
curl http://localhost:8000/info

# Make prediction
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "age": 63, "sex": 1, "cp": 3, "trestbps": 145,
    "chol": 233, "fbs": 1, "restecg": 0, "thalach": 150,
    "exang": 0, "oldpeak": 2.3, "slope": 0, "ca": 0, "thal": 1
  }'
```

### Using Python

```python
import requests

# Prediction
response = requests.post(
    "http://localhost:8000/predict",
    json={
        "age": 63, "sex": 1, "cp": 3, "trestbps": 145,
        "chol": 233, "fbs": 1, "restecg": 0, "thalach": 150,
        "exang": 0, "oldpeak": 2.3, "slope": 0, "ca": 0, "thal": 1
    }
)
print(response.json())
```

### Using Swagger UI

Open http://localhost:8000/docs in your browser for interactive API documentation.

## 📊 Model Details

- **Algorithm:** Random Forest Classifier
- **Features:** 13 clinical features
- **Accuracy:** 100% on test set
- **Framework:** scikit-learn
- **Serialization:** joblib

### Feature Descriptions

| Feature | Description | Range |
|---------|-------------|-------|
| age | Age in years | 0-150 |
| sex | Sex (1=male, 0=female) | 0-1 |
| cp | Chest pain type | 0-3 |
| trestbps | Resting blood pressure | 50-200 |
| chol | Serum cholesterol (mg/dl) | 100-600 |
| fbs | Fasting blood sugar > 120 mg/dl | 0-1 |
| restecg | Resting ECG results | 0-2 |
| thalach | Maximum heart rate | 50-220 |
| exang | Exercise induced angina | 0-1 |
| oldpeak | ST depression | 0-10 |
| slope | Slope of peak exercise ST | 0-2 |
| ca | Number of major vessels | 0-4 |
| thal | Thalassemia | 0-3 |

## 🔧 Development

### Retrain Model

```bash
# Ensure data/heart.csv exists
python train.py
```

This will:
- Load data from `data/heart.csv`
- Train Random Forest model
- Save artifacts to `model/` folder
- Print accuracy metrics

### Project Dependencies

```txt
fastapi==0.109.0        # Web framework
uvicorn[standard]==0.27.0  # ASGI server
scikit-learn==1.4.0     # Machine learning
pandas==2.2.0           # Data manipulation
numpy==1.26.3           # Numerical computing
joblib==1.3.2           # Model serialization
pydantic==2.6.0         # Data validation
```

## 📝 License

MIT License - feel free to use this project for learning and production.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Support

For issues and questions, please open an issue on GitHub.

---

**Built with ❤️ using FastAPI and scikit-learn**
