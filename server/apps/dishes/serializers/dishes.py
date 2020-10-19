from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from apps.dishes.models import Dish, Category


class DishSerializer(ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'image', 'price',
                  'description', 'image_big', 'weight', 'category')


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'id')
