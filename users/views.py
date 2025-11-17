from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .models import Profile, Usage
from .serializers import UserSerializer, ProfileSerializer, UsageSerializer

User = get_user_model()


class CurrentUserView(APIView):
    """Get current authenticated user."""
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class ProfileViewSet(viewsets.ModelViewSet):
    """Profile management."""
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    
    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UsageViewSet(viewsets.ReadOnlyModelViewSet):
    """User usage statistics."""
    serializer_class = UsageSerializer
    queryset = Usage.objects.all()
    
    def get_queryset(self):
        return Usage.objects.filter(user=self.request.user)

