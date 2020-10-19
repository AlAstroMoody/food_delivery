from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.promo.models import Promo
from apps.promo.serializers import PromoSerializer


class PromoViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Promo.objects.all()
    serializer_class = PromoSerializer
