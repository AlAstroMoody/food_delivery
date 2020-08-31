from rest_framework.serializers import ModelSerializer

from apps.promo.models import Promo


class PromoSerializer(ModelSerializer):
    class Meta:
        model = Promo
        fields = 'id', 'name', 'image'

