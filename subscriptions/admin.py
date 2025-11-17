from django.contrib import admin
from .models import Subscription, Invoice, BillingLog


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'plan', 'status', 'started_at', 'expires_at']
    list_filter = ['plan', 'status', 'started_at']
    search_fields = ['user__email']


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'currency', 'status', 'due_date', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['user__email', 'stripe_invoice_id']


@admin.register(BillingLog)
class BillingLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'event_type', 'created_at']
    list_filter = ['event_type', 'created_at']
    search_fields = ['user__email', 'description']
    readonly_fields = ['created_at']

