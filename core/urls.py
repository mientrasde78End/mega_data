from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

# 🔹 DRF Spectacular
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView





urlpatterns = [
    path("admin/", admin.site.urls),

    # Auth
    path("api/auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # OpenAPI Schema
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),

    # Swagger UI
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),

    # Redoc
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),

    # Ecommerce
    path("api/ecommerce/products/", include("ecommerce_products.urls")),
    path("api/ecommerce/users/", include("ecommerce_users.urls")),
    path("api/ecommerce/orders/", include("ecommerce_orders.urls")),
    path("api/ecommerce/payments/", include("ecommerce_payments.urls")),

    # API Products
    path("api/v1/products/", include("Api_products.urls")),

    # Blog
    path("api/blog/auth/", include("blog_accounts.urls")),
    path("api/blog/posts/", include("blog_posts.urls")),

    # Profile / Projects / Contact
    path("api/profile/", include("profile_app.urls")),
    path("api/projects/", include("projects.urls")),
    path("api/contact/", include("contact.urls")),
]

# desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)