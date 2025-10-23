# 🚀 Quick Start Guide

## Test Locally with Docker

### Step 1: Build the Docker Image
```bash
docker-compose build
```

This will:
- Build a multi-stage Docker image
- Install all dependencies
- Copy your model files
- Set up the FastAPI application

### Step 2: Run the Container
```bash
docker-compose up
```

The API will be available at:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

### Step 3: Test the API

**Option A: Use the browser**
1. Open http://localhost:8000/docs
2. Click on `/predict` endpoint
3. Click "Try it out"
4. Use the example payload or modify values
5. Click "Execute"

**Option B: Use the test script**
```bash
# In a new terminal
python test_api.py
```

**Option C: Use cURL**
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "age": 63, "sex": 1, "cp": 3, "trestbps": 145,
    "chol": 233, "fbs": 1, "restecg": 0, "thalach": 150,
    "exang": 0, "oldpeak": 2.3, "slope": 0, "ca": 0, "thal": 1
  }'
```

### Step 4: Stop the Container
```bash
# Press Ctrl+C in the terminal running docker-compose
# Or in another terminal:
docker-compose down
```

---

## Deploy to Render

### Prerequisites
1. GitHub account
2. Render account (free tier available)
3. Your code pushed to a GitHub repository

### Deployment Steps

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Heart Disease API"
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

2. **Go to Render Dashboard**
   - Visit: https://dashboard.render.com/
   - Sign in with your GitHub account

3. **Create New Service**
   - Click "New +" button
   - Select "Blueprint"
   - Connect your GitHub repository
   - Render will detect `render.yaml` automatically

4. **Deploy**
   - Click "Apply"
   - Wait for deployment (usually 2-5 minutes)
   - Your API will be live at: `https://your-service-name.onrender.com`

5. **Test Your Live API**
   - Visit: `https://your-service-name.onrender.com/docs`
   - Test the `/predict` endpoint with sample data

### Monitoring
- **Health Check**: `https://your-service-name.onrender.com/health`
- **Logs**: Available in Render Dashboard
- **Auto-restart**: Enabled by default

---

## Troubleshooting

### Docker Issues

**Problem: Port already in use**
```bash
# Solution: Stop other services or change port in docker-compose.yml
docker-compose down
# Or change "8000:8000" to "8080:8000" in docker-compose.yml
```

**Problem: Build fails**
```bash
# Solution: Clean build cache
docker-compose build --no-cache
```

### API Issues

**Problem: Model not loading**
```bash
# Solution: Verify model files exist
ls -la model/
# Should show: heart_model.joblib, scaler.joblib, feature_names.joblib

# If missing, retrain:
python train.py
```

**Problem: Prediction errors**
- Check input data matches required schema
- All 13 features must be provided
- Values must be within valid ranges (see README.md)

### Render Deployment Issues

**Problem: Build fails on Render**
- Check that all model files are committed to Git
- Verify `render.yaml` configuration
- Check Render logs for specific errors

**Problem: Service crashes**
- Check health endpoint: `/health`
- Review Render logs
- Verify environment variables

---

## Next Steps

1. ✅ Test locally with Docker
2. ✅ Verify all endpoints work
3. ✅ Push to GitHub
4. ✅ Deploy to Render
5. 🎉 Share your API!

**Need help?** Check the main README.md for detailed documentation.
