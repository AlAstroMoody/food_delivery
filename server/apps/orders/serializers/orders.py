from rest_framework.serializers import ModelSerializer

from apps.orders.models import Order, DishInOrder


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = 'id', 'comment', 'status', 'user', 'total_price', 'address', 'phone', 'is_delivery', 'user_name'
        extra_kwargs = {'user': {'read_only': True},
                        'total_price': {'read_only': True}}

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        instance = super().create(validated_data)
        return instance


class DishInOrderSerializer(ModelSerializer):
    class Meta:
        model = DishInOrder
        fields = 'id', 'dish', 'count', 'order', \
                 'price_per_item', 'total_price'
        extra_kwargs = {'price_per_item': {'read_only': True},
                        'total_price': {'read_only': True}}
