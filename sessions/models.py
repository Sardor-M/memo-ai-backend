"""
RecordingSession, ActionItem, and Comment models.
"""
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class RecordingSession(models.Model):
    """Recording session model."""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('recording', 'Recording'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recording_sessions')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    audio_file = models.FileField(upload_to='recordings/', null=True, blank=True)
    transcript = models.TextField(blank=True)
    duration = models.FloatField(default=0.0)  # in seconds
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    started_at = models.DateTimeField(null=True, blank=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'recording_sessions'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.email} - {self.title}"


class ActionItem(models.Model):
    """Action items extracted from recording sessions."""
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    session = models.ForeignKey(RecordingSession, on_delete=models.CASCADE, related_name='action_items')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='action_items')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    due_date = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'action_items'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.session.title}"


class Comment(models.Model):
    """Comments on recording sessions."""
    session = models.ForeignKey(RecordingSession, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comments'
        ordering = ['-created_at']

    def __str__(self):
        return f"Comment by {self.user.email} on {self.session.title}"

