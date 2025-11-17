"""
Supabase JWT authentication for Django REST Framework.
"""
import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import authentication, exceptions
from supabase import create_client, Client

User = get_user_model()


class SupabaseJWTAuthentication(authentication.BaseAuthentication):
    """
    Custom authentication class for Supabase JWT tokens.
    """
    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        
        if not auth_header.startswith('Bearer '):
            return None
        
        token = auth_header.split(' ')[1]
        
        try:
            # Verify token with Supabase
            supabase: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
            user_data = supabase.auth.get_user(token)
            
            if not user_data:
                raise exceptions.AuthenticationFailed('Invalid token')
            
            # Get or create user
            user, created = User.objects.get_or_create(
                supabase_id=user_data.user.id,
                defaults={
                    'email': user_data.user.email,
                    'username': user_data.user.email,
                }
            )
            
            if not created:
                # Update user if needed
                user.email = user_data.user.email
                user.save()
            
            return (user, token)
            
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Token has expired')
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed('Invalid token')
        except Exception as e:
            raise exceptions.AuthenticationFailed(f'Authentication failed: {str(e)}')

