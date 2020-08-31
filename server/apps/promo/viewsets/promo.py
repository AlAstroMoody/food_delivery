from rest_framework.viewsets import ModelViewSet

from apps.promo.models import Promo
from apps.promo.serializers import PromoSerializer


class PromoViewSet(ModelViewSet):
    queryset = Promo.objects.all()
    serializer_class = PromoSerializer
