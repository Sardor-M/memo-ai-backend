from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import RecordingSession, ActionItem, Comment
from .serializers import (
    RecordingSessionSerializer,
    ActionItemSerializer,
    CommentSerializer
)


class RecordingSessionViewSet(viewsets.ModelViewSet):
    """Recording session management."""
    serializer_class = RecordingSessionSerializer
    queryset = RecordingSession.objects.all()
    
    def get_queryset(self):
        return RecordingSession.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    @action(detail=True, methods=['post'])
    def add_comment(self, request, pk=None):
        session = self.get_object()
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(session=session, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActionItemViewSet(viewsets.ModelViewSet):
    """Action item management."""
    serializer_class = ActionItemSerializer
    queryset = ActionItem.objects.all()
    
    def get_queryset(self):
        return ActionItem.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

