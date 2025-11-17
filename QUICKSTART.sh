#!/bin/bash
# 5-minute quick setup

set -e

echo "⚡ Quick Setup - memo-ai-backend"
echo "================================"

# Activate venv if exists, else create
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source venv/bin/activate

# Install dependencies
pip install --upgrade pip -q
pip install -r requirements.txt -q

# Setup .env
if [ ! -f ".env" ]; then
    cp .env.example .env
fi

# Create dirs
mkdir -p logs media staticfiles

# Migrations
python manage.py makemigrations -q
python manage.py migrate -q

echo "✅ Quick setup complete!"
echo "👉 Next: Edit .env and run 'python manage.py runserver'"

