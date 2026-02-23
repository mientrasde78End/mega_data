from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet
from .views2.v2 import ProductViewSetV2  

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="product")
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r'v2/products', ProductViewSetV2, basename='products-v2')

urlpatterns = router.urls
