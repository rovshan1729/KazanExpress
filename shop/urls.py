from django.urls import path, include
from .views import ShopViewSet, ProductViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'shop', ShopViewSet, basename='shop')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'category', CategoryViewSet, basename='category')


urlpatterns = [
    path('api/v1/', include(router.urls)),
]
