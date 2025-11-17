from rest_framework import viewsets
from .models import Subscription, Invoice, BillingLog
from .serializers import (
    SubscriptionSerializer,
    InvoiceSerializer,
    BillingLogSerializer
)


class SubscriptionViewSet(viewsets.ReadOnlyModelViewSet):
    """Subscription management."""
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    
    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)


class InvoiceViewSet(viewsets.ReadOnlyModelViewSet):
    """Invoice management."""
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()
    
    def get_queryset(self):
        return Invoice.objects.filter(user=self.request.user)


class BillingLogViewSet(viewsets.ReadOnlyModelViewSet):
    """Billing log viewing."""
    serializer_class = BillingLogSerializer
    queryset = BillingLog.objects.all()
    
    def get_queryset(self):
        return BillingLog.objects.filter(user=self.request.user)

