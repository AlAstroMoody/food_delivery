from rest_framework import routers

from apps.dishes.viewsets import DishViewSet

router = routers.DefaultRouter()
router.register('dishes', DishViewSet, basename='dishes')
