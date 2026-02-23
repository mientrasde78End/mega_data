from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer
import stripe
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response

stripe.api_key = settings.STRIPE_SECRET_KEY


@api_view(["POST"])
def create_payment_intent(request):
    amount = request.data.get("amount")  # ej: 1000

    # 1️⃣ Crear orden
    order = Order.objects.create(
        total_amount=amount
    )

    # 2️⃣ Crear PaymentIntent en Stripe
    intent = stripe.PaymentIntent.create(
        amount=amount,
        currency="usd",
        automatic_payment_methods={"enabled": True},
        metadata={
            "order_id": order.id
        }
    )

    # 3️⃣ Guardar referencia
    order.stripe_payment_intent = intent.id
    order.save()

    # 4️⃣ Enviar client_secret al frontend
    return Response({
        "clientSecret": intent.client_secret
    })





class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
