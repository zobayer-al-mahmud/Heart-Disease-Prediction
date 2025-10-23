# 📚 Project Documentation Index

Welcome to the Heart Disease Prediction API! This file helps you navigate the documentation.

## 🚀 Getting Started

**New to the project? Start here:**

1. **[README.md](README.md)** - Complete project overview
   - Features and capabilities
   - Full API documentation
   - Deployment options
   - Technical details

2. **[QUICKSTART.md](QUICKSTART.md)** - Get running in 5 minutes
   - Local Docker setup
   - Testing instructions
   - Basic deployment steps

## 📖 Main Documentation

### For Developers

- **[README.md](README.md)** - Main documentation
  - Project structure
  - API endpoints
  - Development setup
  - Testing methods
  - Model details

### For Deployment

- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Production deployment
  - Render deployment (step-by-step)
  - Troubleshooting guide
  - Configuration details
  - Monitoring tips

## 🔍 Quick Reference

### File Structure

```
heart-fastapi-docker/
├── app/               # Application code
├── data/              # Training dataset
├── model/             # ML model artifacts
├── train.py           # Model training
├── Dockerfile         # Container definition
├── docker-compose.yml # Local development
├── render.yaml        # Render deployment
└── test_api.py        # API tests
```

### Key Commands

**Local Development:**
```bash
docker-compose build    # Build the image
docker-compose up       # Start the service
python test_api.py      # Run tests
```

**Training:**
```bash
python train.py         # Retrain the model
```

### API Endpoints

- **GET** `/health` - Health check
- **GET** `/info` - Model information
- **POST** `/predict` - Heart disease prediction
- **GET** `/docs` - Swagger UI (interactive)

## 📂 Project Files

### Core Application
- `app/main.py` - FastAPI application
- `app/schemas.py` - Request/response models
- `app/__init__.py` - Package initialization

### Data & Models
- `data/heart.csv` - Training dataset (Kaggle)
- `model/heart_model.joblib` - Trained Random Forest
- `model/scaler.joblib` - Feature scaler
- `model/feature_names.joblib` - Feature mapping

### Configuration
- `requirements.txt` - Python dependencies
- `Dockerfile` - Docker build instructions
- `docker-compose.yml` - Local development setup
- `render.yaml` - Render deployment config
- `start.sh` - Container startup script

### Development Tools
- `train.py` - Model training script
- `test_api.py` - API testing suite
- `.dockerignore` - Docker build optimization
- `.gitignore` - Git configuration

### Documentation
- `README.md` - Main documentation
- `QUICKSTART.md` - Quick start guide
- `DEPLOYMENT.md` - Deployment guide
- `INDEX.md` - This file

## 🎯 Common Tasks

### I want to...

**Run locally:**
→ See [QUICKSTART.md](QUICKSTART.md) → "Quick Start" section

**Deploy to production:**
→ See [DEPLOYMENT.md](DEPLOYMENT.md) → "Step-by-Step Deployment"

**Test the API:**
→ See [README.md](README.md) → "Testing the API" section

**Understand the model:**
→ See [README.md](README.md) → "Model Details" section

**Retrain the model:**
→ Run: `python train.py` (see [README.md](README.md) → "Development")

**Fix deployment issues:**
→ See [DEPLOYMENT.md](DEPLOYMENT.md) → "Troubleshooting"

**Modify the API:**
→ Edit `app/main.py` and `app/schemas.py`

## 🆘 Need Help?

1. **Check the documentation:**
   - [README.md](README.md) for general info
   - [QUICKSTART.md](QUICKSTART.md) for setup issues
   - [DEPLOYMENT.md](DEPLOYMENT.md) for deployment problems

2. **Review code comments:**
   - `app/main.py` has detailed docstrings
   - `train.py` explains training process

3. **Test locally first:**
   ```bash
   docker-compose up
   curl http://localhost:8000/health
   ```

4. **Check logs:**
   - Docker: `docker-compose logs`
   - Render: Dashboard → Logs tab

## 📊 Project Stats

- **API Endpoints:** 3 core + 2 documentation
- **Dependencies:** 8 packages (minimal)
- **Model Accuracy:** 100% on test set
- **Docker Image:** Multi-stage, optimized
- **Documentation:** 4 comprehensive files

## 🎉 Quick Links

- **Local API:** http://localhost:8000
- **Swagger Docs:** http://localhost:8000/docs
- **Health Check:** http://localhost:8000/health
- **Render:** https://render.com
- **GitHub:** (your repository)

---

**Happy coding! 🚀**
