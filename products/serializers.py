from rest_framework.serializers import ModelSerializer
from .models import Product, Rating, Order, OrderItem
class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'description','category','image', 'price', 'stock_left', 'avg_rating', 'no_of_ratings')


class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(ModelSerializer):
    orderitems_set = OrderItemSerializer(many=True, required = False)
    class Meta:
        model = Order
        fields = '__all__'