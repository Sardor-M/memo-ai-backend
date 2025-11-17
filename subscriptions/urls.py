from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'subscriptions', views.SubscriptionViewSet)
router.register(r'invoices', views.InvoiceViewSet)
router.register(r'logs', views.BillingLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

