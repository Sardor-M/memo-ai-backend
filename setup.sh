#!/bin/bash
# Automated setup script for memo-ai-backend

set -e

echo "Setting up memo-ai-backend..."

# 1. Create virtual environment
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# 2. Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# 3. Upgrade pip
echo "⬆ Upgrading pip..."
pip install --upgrade pip

# 4. Install requirements
echo "🔧 Installing requirements..."
pip install -r requirements.txt

# 5. Copy .env.example to .env if it doesn't exist
if [ ! -f ".env" ]; then
    echo "� Creating .env file from .env.example..."
    cp .env.example .env
    echo "⚠ Please edit .env with your Supabase credentials!"
fi

# 6. Create directories
echo "� Creating directories..."
mkdir -p logs media staticfiles

# 7. Run migrations
echo "� Running database migrations..."
python manage.py makemigrations
python manage.py migrate

# 8. Create superuser (optional)
echo ""
read -p "Create superuser? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    python manage.py createsuperuser
fi

echo ""
echo " Setup complete!"
echo "💡 Don't forget to:"
echo "   1. Edit .env with your Supabase credentials"
echo "   2. Run: python verify_supabase.py to test connection"
echo "   3. Start server: python manage.py runserver"

