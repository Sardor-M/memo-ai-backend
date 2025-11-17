from django.contrib import admin
from .models import RecordingSession, ActionItem, Comment


@admin.register(RecordingSession)
class RecordingSessionAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'status', 'duration', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['title', 'user__email']


@admin.register(ActionItem)
class ActionItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'session', 'user', 'priority', 'status', 'due_date']
    list_filter = ['priority', 'status', 'created_at']
    search_fields = ['title', 'session__title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['session', 'user', 'created_at']
    list_filter = ['created_at']
    search_fields = ['content', 'session__title']

