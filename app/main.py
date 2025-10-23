"""
Heart Disease Prediction API - FastAPI Application
"""
from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
import joblib
import numpy as np
from .schemas import PredictionRequest, PredictionResponse, InfoResponse
import os

# Global variables
model = None
scaler = None
feature_names = None
MODEL_ACCURACY = 1.0

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Load model on startup and cleanup on shutdown"""
    global model, scaler, feature_names
    
    try:
        model_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'heart_model.joblib')
        scaler_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'scaler.joblib')
        features_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'feature_names.joblib')
        
        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)
        feature_names = joblib.load(features_path)
        print("✓ Model loaded successfully")
    except Exception as e:
        print(f"✗ Error loading model: {e}")
        raise
    
    yield
    print("✓ Application shutdown")

# Initialize FastAPI app
app = FastAPI(
    title="Heart Disease Prediction API",
    description="Predict heart disease presence using Random Forest Classifier",
    version="1.0.0",
    lifespan=lifespan
)

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "model_loaded": model is not None
    }

@app.get("/info", response_model=InfoResponse)
async def get_info():
    """Get model information"""
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    return InfoResponse(
        model_type="Random Forest Classifier",
        version="1.0.0",
        features=feature_names,
        accuracy=MODEL_ACCURACY
    )

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    """Make heart disease prediction"""
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    try:
        features = np.array([[
            request.age, request.sex, request.cp, request.trestbps, request.chol,
            request.fbs, request.restecg, request.thalach, request.exang, 
            request.oldpeak, request.slope, request.ca, request.thal
        ]])
        
        features_scaled = scaler.transform(features)
        prediction = model.predict(features_scaled)[0]
        probabilities = model.predict_proba(features_scaled)[0]
        probability = float(probabilities[1])
        
        # Risk level categorization
        if probability >= 0.7:
            risk_level = "high"
        elif probability >= 0.4:
            risk_level = "medium"
        else:
            risk_level = "low"
        
        return PredictionResponse(
            heart_disease=bool(prediction),
            probability=probability,
            risk_level=risk_level
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction error: {str(e)}")

