from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from url_filter.integrations.drf import DjangoFilterBackend

from apps.main.permissions import IsUserAddThisDishForThisOrder
from apps.orders.models import Order, DishInOrder
from apps.orders.serializers import OrderSerializer, DishInOrderSerializer


class OrderViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class DishInOrderViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = DishInOrder.objects.all()
    serializer_class = DishInOrderSerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (IsUserAddThisDishForThisOrder,)
    filter_fields = ('order',)
