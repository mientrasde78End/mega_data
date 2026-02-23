from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet
from .views import create_payment_intent


router = DefaultRouter()
router.register("", OrderViewSet, basename="orders")

urlpatterns = [
    path("", include(router.urls)),
    path("create-payment-intent/", create_payment_intent),
]
