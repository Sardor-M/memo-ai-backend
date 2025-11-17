from rest_framework import serializers
from .models import RecordingSession, ActionItem, Comment
from users.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']


class ActionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionItem
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']


class RecordingSessionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    action_items = ActionItemSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = RecordingSession
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']

