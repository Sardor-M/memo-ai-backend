from django.apps import AppConfig


class SessionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sessions'
    label = 'recording_sessions'  # Custom label to avoid conflict with Django's built-in sessions

