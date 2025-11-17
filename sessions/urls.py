from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'sessions', views.RecordingSessionViewSet)
router.register(r'action-items', views.ActionItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

