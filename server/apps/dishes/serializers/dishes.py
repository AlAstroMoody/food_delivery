from rest_framework.serializers import ModelSerializer

from apps.dishes.models import Dish


class DishSerializer(ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'image', 'price', 'description', 'image_big', 'weight')
