from rest_framework import routers

from apps.dishes.viewsets import DishViewSet
from apps.dishes.viewsets import CategoryViewSet
from apps.profile.viewsets import ProfileViewSet
from apps.users.viewsets import RegisterViewSet
from apps.users.viewsets import AuthViewSet
from apps.orders.viewsets import OrderViewSet, DishInOrderViewSet
from apps.promo.viewsets import PromoViewSet

router = routers.DefaultRouter()
router.register('dishes', DishViewSet, basename='dishes')
router.register('category', CategoryViewSet, basename='category')
router.register('register', RegisterViewSet, basename='register')
router.register('auth/token', AuthViewSet, basename='auth')
router.register('orders', OrderViewSet, basename='orders')
router.register('dish_in_order', DishInOrderViewSet, basename='dish_in_order')
router.register('promo', PromoViewSet, basename='promo')
router.register('profile', ProfileViewSet, basename='profile')
