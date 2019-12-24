from api.models import Order, Product
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['id', 'price', 'shop']

    def create(self, validated_data):
        product = validated_data['product']
        total_amount = product.price * validated_data['qy']

        validated_data.update(
            {
                'price': total_amount,
                'shop': product.shop,
            }
        )

        return Order.objects.create(**validated_data)
