from rest_framework.viewsets import ModelViewSet
from Api_products.models import Product
from Api_products.serializers import ProductSerializer
from Api_products.pagination import ProductPagination
from Api_products.filters import ProductFilter


class ProductViewSetV2(ModelViewSet):
    """
    Versión 2 del API de productos
    Cambios:
    - Incluye productos inactivos
    - Ordena por fecha descendente por defecto
    """

    serializer_class = ProductSerializer
    lookup_field = "slug"
    pagination_class = ProductPagination
    filterset_class = ProductFilter

    ordering = ["-created_at"]
    search_fields = ["name", "description"]

    def get_queryset(self):
        return Product.objects.all()  # ← diferencia clave con v1
