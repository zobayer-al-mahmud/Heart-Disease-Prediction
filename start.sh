#!/bin/sh
# Startup script for Render deployment
# Uses PORT environment variable if available, defaults to 8000

PORT=${PORT:-8000}
echo "Starting uvicorn on port $PORT"
exec uvicorn app.main:app --host 0.0.0.0 --port "$PORT"
