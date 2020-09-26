from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.viewsets import mixins, GenericViewSet

from apps.dishes.models import Dish, Category
from apps.dishes.serializers import DishSerializer, CategorySerializer
from config.settings import CACHE_TTL


class DishViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

    @method_decorator(cache_page(CACHE_TTL))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class CategoryViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
