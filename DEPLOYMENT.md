# Deployment Guide - Render

This guide walks you through deploying your Heart Disease Prediction API to Render.

## Prerequisites

- [ ] GitHub account
- [ ] Render account (sign up at https://render.com - free tier available)
- [ ] Your code pushed to a GitHub repository

## Step-by-Step Deployment

### 1. Prepare Your Repository

Make sure all files are committed and pushed to GitHub:

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: Heart Disease Prediction API"

# Add remote (replace with your repo URL)
git remote add origin https://github.com/yourusername/heart-disease-api.git

# Push to GitHub
git push -u origin main
```

### 2. Sign Up for Render

1. Go to https://render.com
2. Click "Get Started" or "Sign Up"
3. Sign up using your GitHub account (recommended)
4. Authorize Render to access your repositories

### 3. Deploy Using Blueprint (Recommended)

Since we have a `render.yaml` file, Render will automatically configure everything:

1. **Go to Render Dashboard**
   - https://dashboard.render.com/

2. **Create New Blueprint**
   - Click "New +" button (top right)
   - Select "Blueprint"

3. **Connect Repository**
   - Select your GitHub repository
   - Grant access if needed
   - Render will detect `render.yaml`

4. **Review Configuration**
   - Service Name: `heart-disease-api`
   - Environment: Docker
   - Plan: Free
   - Region: Oregon (or your preference)

5. **Deploy!**
   - Click "Apply"
   - Wait 2-5 minutes for deployment
   - Your API will be live!

### 4. Alternative: Manual Web Service Setup

If you prefer manual setup:

1. **Create Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository

2. **Configure Settings**
   ```
   Name: heart-disease-api
   Environment: Docker
   Region: Oregon
   Branch: main
   ```

3. **Advanced Settings**
   ```
   Health Check Path: /health
   Auto-Deploy: Yes
   ```

4. **Create Web Service**
   - Click "Create Web Service"
   - Deployment starts automatically

## Post-Deployment

### Access Your API

Once deployed, your API will be available at:
```
https://heart-disease-api.onrender.com
```

**Test the endpoints:**
- Health: https://your-service.onrender.com/health
- Docs: https://your-service.onrender.com/docs
- Info: https://your-service.onrender.com/info

### Monitor Your Service

1. **View Logs**
   - Dashboard → Your Service → Logs tab
   - Real-time logs of requests and errors

2. **Check Health**
   - Dashboard → Your Service → Events tab
   - Health check status
   - Deploy history

3. **Metrics** (Free tier limited)
   - CPU usage
   - Memory usage
   - Request count

### Test Your Live API

**Using cURL:**
```bash
# Health check
curl https://your-service.onrender.com/health

# Get model info
curl https://your-service.onrender.com/info

# Make prediction
curl -X POST https://your-service.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d '{
    "age": 63, "sex": 1, "cp": 3, "trestbps": 145,
    "chol": 233, "fbs": 1, "restecg": 0, "thalach": 150,
    "exang": 0, "oldpeak": 2.3, "slope": 0, "ca": 0, "thal": 1
  }'
```

**Using Python:**
```python
import requests

BASE_URL = "https://your-service.onrender.com"

# Make prediction
response = requests.post(
    f"{BASE_URL}/predict",
    json={
        "age": 63, "sex": 1, "cp": 3, "trestbps": 145,
        "chol": 233, "fbs": 1, "restecg": 0, "thalach": 150,
        "exang": 0, "oldpeak": 2.3, "slope": 0, "ca": 0, "thal": 1
    }
)
print(response.json())
```

## Configuration Details

### Environment Variables

The following are automatically configured via `render.yaml`:

```yaml
PORT: 8000              # Render will override with their port
PYTHONUNBUFFERED: 1     # For better logging
```

No additional environment variables needed!

### Health Checks

Render automatically monitors your `/health` endpoint:
- **Interval**: Every 30 seconds
- **Timeout**: 10 seconds
- **Expected**: 200 status code

If health checks fail 3 times, Render will restart your service.

### Auto-Deploy

By default, Render auto-deploys on every push to your `main` branch:
1. Push code to GitHub
2. Render detects changes
3. Automatic rebuild and deploy
4. Zero-downtime deployment

To disable:
- Dashboard → Service → Settings → Auto-Deploy → Off

## Troubleshooting

### Issue: Build Fails

**Check:**
1. All files committed (especially model files)
2. Dockerfile syntax correct
3. requirements.txt has all dependencies

**Solution:**
```bash
# Verify files in Git
git ls-files

# Should include:
# - Dockerfile
# - requirements.txt
# - app/main.py, app/schemas.py
# - model/*.joblib
```

### Issue: Service Crashes

**Check logs:**
1. Dashboard → Your Service → Logs
2. Look for Python errors or missing files

**Common issues:**
- Model files not found → Verify in Git
- Import errors → Check requirements.txt
- Port binding errors → start.sh handles this

### Issue: Health Check Fails

**Verify:**
```bash
# Test locally first
docker-compose up
curl http://localhost:8000/health
```

**Check:**
- `/health` endpoint returns 200
- Response time < 10 seconds
- Service starts successfully

### Issue: Slow First Request (Cold Start)

**This is normal for free tier:**
- First request after inactivity takes ~30 seconds
- Subsequent requests are fast
- Render spins down free services after 15 min inactivity

**Solution for production:**
- Upgrade to paid plan ($7/month)
- Keeps service always running

## Costs

### Free Tier Includes:
- ✅ 750 hours/month (enough for one service 24/7)
- ✅ Automatic HTTPS
- ✅ Custom domains
- ✅ Auto-deploy from Git
- ✅ Health checks
- ⚠️ Spins down after 15 min inactivity
- ⚠️ 100 GB bandwidth/month

### Paid Plan ($7/month):
- ✅ Always running (no spin down)
- ✅ Faster deploys
- ✅ More resources
- ✅ Priority support

## Updating Your API

### Deploy New Changes

```bash
# Make your changes
git add .
git commit -m "Update: description of changes"
git push

# Render auto-deploys in ~2 minutes
```

### Rollback to Previous Version

1. Dashboard → Service → Events
2. Find successful deploy
3. Click "Rollback"

## Custom Domain (Optional)

1. Dashboard → Service → Settings
2. Custom Domain section
3. Add your domain
4. Update DNS records (shown by Render)
5. Wait for SSL certificate (automatic)

## Best Practices

1. **Always test locally first**
   ```bash
   docker-compose build
   docker-compose up
   curl http://localhost:8000/health
   ```

2. **Use environment-specific settings**
   - Development: docker-compose
   - Production: render.yaml

3. **Monitor logs regularly**
   - Check for errors
   - Monitor response times
   - Track usage patterns

4. **Keep model files in Git**
   - Model artifacts must be committed
   - Use Git LFS for large files if needed

5. **Version your API**
   - Update version in app/main.py
   - Tag releases in Git

## Support

- **Render Documentation**: https://render.com/docs
- **Render Community**: https://community.render.com
- **GitHub Issues**: (your repo)

## Summary Checklist

- [ ] Code pushed to GitHub
- [ ] Render account created
- [ ] Repository connected to Render
- [ ] Service deployed successfully
- [ ] Health endpoint returns 200
- [ ] API docs accessible at /docs
- [ ] Test prediction endpoint
- [ ] Logs show no errors
- [ ] Bookmark service URL
- [ ] Set up monitoring (optional)

---

**Congratulations! Your API is now live! 🎉**

Access your API at: https://your-service.onrender.com/docs
