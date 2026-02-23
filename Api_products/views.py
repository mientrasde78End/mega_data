import rest_framework.viewsets
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .filters import ProductFilter
from .pagination import ProductPagination


class CategoryViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(rest_framework.viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    lookup_field = "slug"
    pagination_class = ProductPagination
    filterset_class = ProductFilter

    search_fields = ["name", "description"]
    ordering_fields = ["price", "created_at"]


    def get_queryset(self):
        return Product.objects.filter(is_active=True)
    
    @action(detail=True, methods=["post"])
    def restore(self, request, slug=None):
        product = Product.objects.filter(slug=slug).first()

        if not product:
            return Response(
                {"error": "Producto no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )

        product.restore()
        return Response(
            {"status": "Producto restaurado"},
            status=status.HTTP_200_OK
        )
