from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from url_filter.integrations.drf import DjangoFilterBackend

from apps.orders.models import Order, DishInOrder
from apps.orders.serializers import OrderSerializer, DishInOrderSerializer


class OrderViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                   mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class DishInOrderViewSet(ModelViewSet):
    queryset = DishInOrder.objects.all()
    serializer_class = DishInOrderSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('order',)
