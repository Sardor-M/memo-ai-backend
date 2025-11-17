#!/usr/bin/env python
"""
Verify Supabase connection and configuration.
"""
import os
import sys
import django
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables before Django setup
BASE_DIR = Path(__file__).resolve().parent
env_file = BASE_DIR / '.env'
if env_file.exists():
    load_dotenv(env_file)

# Setup Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'memo_ai_backend.settings')
django.setup()

from django.conf import settings
from supabase import create_client, Client
from psycopg2 import connect, OperationalError


def verify_supabase_client():
    """Verify Supabase client connection."""
    print("Verifying Supabase Client...")
    
    if not settings.SUPABASE_URL:
        print("ERROR: SUPABASE_URL not set in environment")
        return False
    
    if not settings.SUPABASE_KEY:
        print("ERROR: SUPABASE_KEY not set in environment")
        return False
    
    try:
        supabase: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
        print("SUCCESS: Supabase client created successfully")
        print(f"URL: {settings.SUPABASE_URL}")
        return True
    except Exception as e:
        print(f"ERROR: Failed to create Supabase client: {e}")
        return False


def verify_database():
    """Verify PostgreSQL database connection."""
    print("\nVerifying Database Connection...")
    
    db_config = settings.DATABASES['default']
    print(f"Host: {db_config.get('HOST', 'Not set')}")
    print(f"Port: {db_config.get('PORT', 'Not set')}")
    print(f"Database: {db_config.get('NAME', 'Not set')}")
    print(f"User: {db_config.get('USER', 'Not set')}")
    
    try:
        conn = connect(
            host=db_config.get('HOST', 'localhost'),
            port=db_config.get('PORT', 5432),
            database=db_config.get('NAME', 'postgres'),
            user=db_config.get('USER', 'postgres'),
            password=db_config.get('PASSWORD', ''),
        )
        conn.close()
        print("SUCCESS: Database connection successful")
        return True
    except OperationalError as e:
        print(f"ERROR: Database connection failed: {e}")
        print("\nTips:")
        print("- Verify your database host in .env file")
        print("- Check if you're using the session pooler connection string")
        print("- Ensure your IP is whitelisted in Supabase dashboard")
        return False
    except Exception as e:
        print(f"ERROR: Unexpected error: {e}")
        return False


def main():
    """Run all verification checks."""
    print("=" * 50)
    print("Supabase Configuration Verification")
    print("=" * 50)
    
    client_ok = verify_supabase_client()
    db_ok = verify_database()
    
    print("\n" + "=" * 50)
    if client_ok and db_ok:
        print("All checks passed!")
        sys.exit(0)
    else:
        print("Some checks failed. Please review your configuration.")
        sys.exit(1)


if __name__ == '__main__':
    main()
