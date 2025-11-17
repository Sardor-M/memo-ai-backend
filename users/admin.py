from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Profile, Usage, AuditLog


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'username', 'is_verified', 'created_at']
    list_filter = ['is_verified', 'is_staff', 'is_superuser']
    search_fields = ['email', 'username']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'company']
    search_fields = ['user__email', 'first_name', 'last_name']


@admin.register(Usage)
class UsageAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'recordings_count', 'minutes_recorded']
    list_filter = ['date']
    search_fields = ['user__email']


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'action', 'resource_type', 'created_at']
    list_filter = ['action', 'resource_type', 'created_at']
    search_fields = ['user__email', 'description']
    readonly_fields = ['created_at']

