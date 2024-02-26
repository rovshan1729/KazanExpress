from rest_framework.permissions import BasePermission

class ShopAdminPermission(BasePermission):
    def has_permission(self, request, view):

        return True
    

class ProductAdminPermission(BasePermission):
    def has_permission(self, request, view):

        return True
    

class CategoryAdminPermission(BasePermission):
    def has_permission(self, request, view):

        return True
    
    
class ProductModeratorPermission(BasePermission):
    def has_permission(self, request, view):
       
        return request.user and request.user.is_authenticated and request.user.is_product_moderator

class PageModeratorPermission(BasePermission):
    def has_permission(self, request, view):
       
        return request.user and request.user.is_authenticated and request.user.is_page_moderator
