# Memo AI Backend

Django REST API backend for Memo AI software. A full backend system for managing users, recording sessions, action items, and subscriptions.

## Features

- **User Authentication** - Supabase JWT-based authentication
- **Recording Session Management** - Track and manage audio recordings
- **Action Item Tracking** - Extract and manage action items from sessions
- **Subscription & Billing** - Complete subscription and invoice management
- **Usage Analytics** - Track user usage metrics
- **Audit Logging** - Comprehensive audit trail for user actions
- **PostgreSQL Database** - Powered by Supabase

## Tech Stack

- **Framework**: Django 4.2+
- **API**: Django REST Framework
- **Database**: PostgreSQL (Supabase)
- **Authentication**: Supabase JWT
- **Image Processing**: Pillow
- **CORS**: django-cors-headers

### Dependencies

```
Django>=4.2.0,<5.0.0
djangorestframework>=3.14.0
psycopg2-binary>=2.9.0
supabase>=2.0.0
postgrest>=0.13.0
python-dotenv>=1.0.0
django-cors-headers>=4.3.0
Pillow>=10.0.0
```

## Quick Start

### Option 1: Quick Setup (5 minutes)

```bash
bash QUICKSTART.sh
```

### Option 2: Automated Setup

```bash
bash setup.sh
```

### Option 3: Manual Setup

```bash
# 1. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 3. Configure environment
cp .env.example .env
# Edit .env with your Supabase credentials

# 4. Create directories
mkdir -p logs media staticfiles

# 5. Run migrations
python manage.py makemigrations
python manage.py migrate

# 6. Create superuser
python manage.py createsuperuser

# 7. Verify Supabase connection
python verify_supabase.py

# 8. Start server
python manage.py runserver
```

## API Endpoints

All API endpoints require authentication via Supabase JWT token in the `Authorization` header:
```
Authorization: Bearer <your-jwt-token>
```

### Base URL
```
http://localhost:8000/api
```

### User Management (`/api/users/`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/users/me/` | Get current authenticated user |
| `GET` | `/api/users/profiles/` | List user profiles |
| `POST` | `/api/users/profiles/` | Create user profile |
| `GET` | `/api/users/profiles/{id}/` | Get profile details |
| `PUT` | `/api/users/profiles/{id}/` | Update profile |
| `PATCH` | `/api/users/profiles/{id}/` | Partially update profile |
| `DELETE` | `/api/users/profiles/{id}/` | Delete profile |
| `GET` | `/api/users/usage/` | List usage statistics |
| `GET` | `/api/users/usage/{id}/` | Get usage details |

### Recording Sessions (`/api/sessions/`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/sessions/sessions/` | List recording sessions |
| `POST` | `/api/sessions/sessions/` | Create new recording session |
| `GET` | `/api/sessions/sessions/{id}/` | Get session details |
| `PUT` | `/api/sessions/sessions/{id}/` | Update session |
| `PATCH` | `/api/sessions/sessions/{id}/` | Partially update session |
| `DELETE` | `/api/sessions/sessions/{id}/` | Delete session |
| `POST` | `/api/sessions/sessions/{id}/add_comment/` | Add comment to session |
| `GET` | `/api/sessions/action-items/` | List action items |
| `POST` | `/api/sessions/action-items/` | Create action item |
| `GET` | `/api/sessions/action-items/{id}/` | Get action item details |
| `PUT` | `/api/sessions/action-items/{id}/` | Update action item |
| `PATCH` | `/api/sessions/action-items/{id}/` | Partially update action item |
| `DELETE` | `/api/sessions/action-items/{id}/` | Delete action item |

### Subscriptions & Billing (`/api/subscriptions/`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/subscriptions/subscriptions/` | List subscriptions |
| `GET` | `/api/subscriptions/subscriptions/{id}/` | Get subscription details |
| `GET` | `/api/subscriptions/invoices/` | List invoices |
| `GET` | `/api/subscriptions/invoices/{id}/` | Get invoice details |
| `GET` | `/api/subscriptions/logs/` | List billing logs |
| `GET` | `/api/subscriptions/logs/{id}/` | Get billing log details |

### Admin Panel

| Endpoint | Description |
|----------|-------------|
| `/admin/` | Django admin interface |

## Project Structure

```
memo-ai-backend/
├── manage.py                 # Django CLI
├── requirements.txt          # Python dependencies
├── .env.example              # Environment variables template
├── Dockerfile               # Production Docker image
├── docker-compose.yml       # Local development setup
├── verify_supabase.py       # Test Supabase connection
├── setup.sh                 # Automated setup script
├── QUICKSTART.sh            # Quick setup script
│
├── memo_ai_backend/         # Main project configuration
│   ├── __init__.py
│   ├── settings.py          # Django settings with Supabase config
│   ├── urls.py              # Root URL routing
│   ├── wsgi.py              # WSGI application
│   └── asgi.py              # ASGI application
│
├── users/                   # User management app
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py            # User, Profile, Usage, AuditLog models
│   ├── authentication.py    # Supabase JWT authentication
│   ├── views.py             # API views
│   ├── serializers.py       # DRF serializers
│   ├── urls.py              # User app URLs
│   └── admin.py             # Django admin configuration
│
├── sessions/                # Recording sessions app
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py            # RecordingSession, ActionItem, Comment models
│   ├── views.py             # API views
│   ├── serializers.py       # DRF serializers
│   ├── urls.py              # Sessions app URLs
│   └── admin.py             # Django admin configuration
│
├── subscriptions/           # Billing & subscriptions app
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py            # Subscription, Invoice, BillingLog models
│   ├── views.py             # API views
│   ├── serializers.py       # DRF serializers
│   ├── urls.py              # Subscriptions app URLs
│   └── admin.py             # Django admin configuration
│
├── logs/                    # Application logs
├── media/                   # User uploaded files
└── staticfiles/             # Collected static files
```

## File Reference

### Core Files

- `manage.py` - Django CLI for running commands
- `requirements.txt` - Python package dependencies
- `.env.example` - Environment variables template (copy to `.env`)

### Configuration

- `memo_ai_backend/settings.py` - Complete Django settings with Supabase integration
- `memo_ai_backend/urls.py` - Root URL routing configuration
- `memo_ai_backend/wsgi.py` - WSGI interface for production servers

### Apps

#### users/
- `models.py` - User, Profile, Usage, AuditLog models
- `authentication.py` - Supabase JWT authentication middleware
- `views.py` - User, Profile, Usage API views
- `serializers.py` - Data serialization for API
- `urls.py` - User management routes
- `admin.py` - Django admin interface configuration

#### sessions/
- `models.py` - RecordingSession, ActionItem, Comment models
- `views.py` - Recording session and action item API views
- `serializers.py` - Data serialization for API
- `urls.py` - Session management routes
- `admin.py` - Django admin interface configuration

#### subscriptions/
- `models.py` - Subscription, Invoice, BillingLog models
- `views.py` - Subscription and billing API views
- `serializers.py` - Data serialization for API
- `urls.py` - Subscription management routes
- `admin.py` - Django admin interface configuration

### Scripts

- `verify_supabase.py` - Test Supabase connection and database
- `setup.sh` - Automated project setup script
- `QUICKSTART.sh` - Quick 5-minute setup script

## Database Models

### Users App
- **User** - Custom user model with Supabase integration
- **Profile** - Extended user profile information
- **Usage** - Daily usage metrics tracking
- **AuditLog** - Audit trail for user actions

### Sessions App
- **RecordingSession** - Audio recording sessions
- **ActionItem** - Action items extracted from sessions
- **Comment** - Comments on recording sessions

### Subscriptions App
- **Subscription** - User subscription plans
- **Invoice** - Billing invoices
- **BillingLog** - Billing event logs

## Environment Variables

Create a `.env` file from `.env.example` and configure:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Supabase Configuration
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-key-here
SUPABASE_SERVICE_KEY=your-service-role-key-here

# Database (Supabase PostgreSQL)
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=your-db-password
DB_HOST=db.your-project.supabase.co
DB_PORT=5432

# CORS
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000
```

## Development

### Running the Server

```bash
python manage.py runserver
```

### Running Migrations

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

### Creating Superuser

```bash
python manage.py createsuperuser
```

### Verifying Supabase Connection

```bash
python verify_supabase.py
```

## Docker Support

### Development with Docker Compose

```bash
docker-compose up
```

### Production Build

```bash
docker build -t memo-ai-backend .
docker run -p 8000:8000 memo-ai-backend
```

## Authentication

The API uses Supabase JWT authentication. Include the token in requests:

```bash
curl -H "Authorization: Bearer <your-jwt-token>" \
     http://localhost:8000/api/users/me/
```

## Pagination

All list endpoints support pagination with 20 items per page by default.

## Documentation

- [Complete Setup Guide](COMPLETE_SETUP_GUIDE.md) - Detailed installation instructions
- [Supabase Setup](SUPABASE_SETUP.md) - Supabase configuration guide
- [File Reference](FILE_REFERENCE.md) - Detailed file descriptions
- [Index](INDEX.md) - Project structure overview

## License

MIT License

## Support or Contact

Email: sardor0968@gmail.com
