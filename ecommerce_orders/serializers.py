from rest_framework import serializers
from .models import Order, OrderItem
from ecommerce_products.models import Product

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ("product", "quantity")

    def validate(self, data):
        product = data["product"]
        quantity = data["quantity"]

        if quantity <= 0:
            raise serializers.ValidationError("Quantity must be greater than 0")

        if product.stock < quantity:
            raise serializers.ValidationError("Not enough stock")

        return data


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ("id", "status", "items", "total", "created_at")

    def get_total(self, obj):
        return obj.get_total()

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        user = self.context["request"].user

        order = Order.objects.create(user=user)

        for item in items_data:
            product = item["product"]
            quantity = item["quantity"]

            product.stock -= quantity
            product.save()

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity
            )

        return order
