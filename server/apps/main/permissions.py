from rest_framework import permissions


class IsUserProfile(permissions.BasePermission):
    # разрешать, если профиль именно клиента
    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True


class IsUserCreateThisOrder(permissions.BasePermission):
    # разрешать, если это заказ текущего клиента
    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True


class IsUserAddThisDishForThisOrder(permissions.BasePermission):
    # разрешать, если это заказ текущего клиента
    def has_object_permission(self, request, view, obj):
        if obj.order.user == request.user:
            return True
