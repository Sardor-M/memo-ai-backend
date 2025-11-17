from rest_framework import serializers
from .models import Subscription, Invoice, BillingLog
from users.serializers import UserSerializer


class SubscriptionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Subscription
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']


class InvoiceSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Invoice
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']


class BillingLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingLog
        fields = '__all__'
        read_only_fields = ['user', 'created_at']

