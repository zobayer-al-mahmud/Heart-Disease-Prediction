"""
Pydantic models for Heart Disease Prediction API
"""
from pydantic import BaseModel, Field


class PredictionRequest(BaseModel):
    """Input model for heart disease prediction"""
    age: int = Field(..., ge=0, le=150, description="Age in years")
    sex: int = Field(..., ge=0, le=1, description="0=female, 1=male")
    cp: int = Field(..., ge=0, le=3, description="Chest pain type")
    trestbps: int = Field(..., ge=0, le=300, description="Resting blood pressure")
    chol: int = Field(..., ge=0, le=600, description="Serum cholesterol")
    fbs: int = Field(..., ge=0, le=1, description="Fasting blood sugar > 120")
    restecg: int = Field(..., ge=0, le=2, description="Resting ECG results")
    thalach: int = Field(..., ge=0, le=250, description="Max heart rate achieved")
    exang: int = Field(..., ge=0, le=1, description="Exercise-induced angina")
    oldpeak: float = Field(..., ge=0.0, le=10.0, description="ST depression")
    slope: int = Field(..., ge=0, le=2, description="ST segment slope")
    ca: int = Field(..., ge=0, le=3, description="Major vessels colored")
    thal: int = Field(..., ge=0, le=3, description="Thalassemia")


class PredictionResponse(BaseModel):
    """Output model for prediction"""
    heart_disease: bool = Field(..., description="Disease present (true/false)")
    probability: float = Field(..., description="Confidence probability (0-1)")
    risk_level: str = Field(..., description="Risk level (low/medium/high)")


class InfoResponse(BaseModel):
    """Model information response"""
    model_type: str = Field(..., description="ML model type")
    version: str = Field(..., description="API version")
    features: list = Field(..., description="Feature names")
    accuracy: float = Field(..., description="Model accuracy")
