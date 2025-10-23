"""
Train and save the heart disease prediction model
Run with: python train.py
"""
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import os

# Load dataset
df = pd.read_csv('data/heart.csv')
print(f"Dataset shape: {df.shape}")

# Prepare data
X = df.drop('target', axis=1)
y = df['target']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
print("Training Random Forest Classifier...")
model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train_scaled, y_train)

# Evaluate
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print(f"\n✓ Model Accuracy: {accuracy:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save artifacts
os.makedirs('model', exist_ok=True)
joblib.dump(model, 'model/heart_model.joblib')
joblib.dump(scaler, 'model/scaler.joblib')
joblib.dump(X.columns.tolist(), 'model/feature_names.joblib')

print("\n✓ Model saved to model/heart_model.joblib")
print("✓ Scaler saved to model/scaler.joblib")
print("✓ Feature names saved to model/feature_names.joblib")
