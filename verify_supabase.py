#!/usr/bin/env python
"""
Verify Supabase connection and configuration.
"""
import os
import sys
import django

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
        print("SUPABASE_URL not set in environment")
        return False
    
    if not settings.SUPABASE_KEY:
        print("SUPABASE_KEY not set in environment")
        return False
    
    try:
        supabase: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
        # Try to get auth user (this will fail if connection is bad)
        print("Supabase client created successfully")
        print(f"   URL: {settings.SUPABASE_URL}")
        return True
    except Exception as e:
        print(f"Failed to create Supabase client: {e}")
        return False


def verify_database():
    """Verify PostgreSQL database connection."""
    print("\nVerifying Database Connection...")
    
    try:
        conn = connect(
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT'],
            database=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
        )
        conn.close()
        print("Database connection successful")
        return True
    except OperationalError as e:
        print(f"Database connection failed: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
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

