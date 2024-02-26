from .models import Shop, Product, Category
from .serializers import ShopSerializer, ProductSerializer, CategorySerializer
from rest_framework import viewsets, filters, pagination
from .permissions import ShopAdminPermission, ProductAdminPermission, CategoryAdminPermission
from rest_framework.permissions import IsAdminUser

class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [IsAdminUser]
    search_fields = ('title',)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [ProductAdminPermission]
    pagination_class = pagination.PageNumberPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ('amount', 'price')
    filterset_fields = ('active', 'price',)
    search_fields = ('id', 'title',)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CategoryAdminPermission]
    pagination_class = pagination.PageNumberPagination
    search_fields = ('title', 'id', 'parent')



