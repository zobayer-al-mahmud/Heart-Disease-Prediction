"""
Simple test script to verify the API endpoints
Run with: python test_api.py
"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_health():
    """Test health endpoint"""
    print("\n1. Testing /health endpoint...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    assert response.status_code == 200
    print("✓ Health check passed")

def test_info():
    """Test info endpoint"""
    print("\n2. Testing /info endpoint...")
    response = requests.get(f"{BASE_URL}/info")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 200
    print("✓ Info endpoint passed")

def test_predict():
    """Test predict endpoint"""
    print("\n3. Testing /predict endpoint...")
    
    # Sample patient data
    patient_data = {
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
    
    response = requests.post(f"{BASE_URL}/predict", json=patient_data)
    print(f"Status: {response.status_code}")
    print(f"Request: {json.dumps(patient_data, indent=2)}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 200
    print("✓ Prediction endpoint passed")

if __name__ == "__main__":
    print("="*60)
    print("Heart Disease Prediction API - Test Suite")
    print("="*60)
    
    try:
        test_health()
        test_info()
        test_predict()
        
        print("\n" + "="*60)
        print("✓ All tests passed!")
        print("="*60)
    except requests.exceptions.ConnectionError:
        print("\n✗ Error: Cannot connect to API")
        print("Make sure the API is running: docker-compose up")
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
