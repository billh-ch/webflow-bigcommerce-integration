#!/bin/bash
# Startup script for Webflow-BigCommerce Integration Plugin

set -e

echo "Starting Webflow-BigCommerce Integration Plugin..."

# Check if virtual environment exists, create if not
if [ ! -d "venv" ]; then
  echo "Creating virtual environment..."
  python3 -m venv venv
  source venv/bin/activate
  pip install -r backend/requirements.txt
else
  source venv/bin/activate
fi

# Check if required environment variables are set
if [ -z "$BIGCOMMERCE_STORE_HASH" ] || [ -z "$BIGCOMMERCE_ACCESS_TOKEN" ] || [ -z "$WEBFLOW_API_KEY" ] || [ -z "$WEBFLOW_SITE_ID" ]; then
  echo "Error: Required environment variables are not set."
  echo "Please set:"
  echo "  BIGCOMMERCE_STORE_HASH"
  echo "  BIGCOMMERCE_ACCESS_TOKEN"
  echo "  WEBFLOW_API_KEY"
  echo "  WEBFLOW_SITE_ID"
  exit 1
fi

# Start the application
echo "Starting server on port ${PORT:-5000}..."
cd backend
gunicorn --bind 0.0.0.0:${PORT:-5000} --workers 4 app:app