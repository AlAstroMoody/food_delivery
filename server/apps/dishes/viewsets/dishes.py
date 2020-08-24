from rest_framework.viewsets import mixins, GenericViewSet

from apps.dishes.models import Dish
from apps.dishes.serializers import DishSerializer


class DishViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
