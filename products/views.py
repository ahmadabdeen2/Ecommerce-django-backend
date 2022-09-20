from django.shortcuts import render
from .serializers import ProductSerializer, RatingSerializer, OrderSerializer, OrderItemSerializer
from rest_framework import viewsets
from .models import Product, Rating, Order, OrderItem
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    # permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    
    # def get_queryset(self):
    #     return Order.objects.filter(user=self.request.user)


class OrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()