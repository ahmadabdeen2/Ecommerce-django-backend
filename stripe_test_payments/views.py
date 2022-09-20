from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes

from rest_framework import status
from rest_framework.response import Response
import json

import stripe

stripe.api_key = 'sk_test_51LirZXBJl49q98MGbBAWnLXiJsBuwYNy3ygCe2eTHGIUFI2mbMA4pil1CS12UM1As6h3hbfkjEmartnWSRCMiCC7005iJcsSPg'

@api_view(['POST'])
def test_payment(request):
    test_payment_intent = stripe.PaymentIntent.create(
    amount=1000, currency='pln', 
    payment_method_types=['card'],
    receipt_email='test@example.com')
    return Response(status=status.HTTP_200_OK, data=test_payment_intent)
@api_view(['POST'])
@csrf_exempt
def save_stripe_info(request):
    data = request.data
    email = data['email']
    payment_method_id = data['payment_method_id']
    customer_data = stripe.Customer.list(email=email).data   
    if len(customer_data) == 0:
      customer = stripe.Customer.create(
      email=email, payment_method=payment_method_id)
    else:
      customer = customer_data[0]
      extra_msg = 'Customer already exists'
    stripe.PaymentIntent.create(
    customer=customer, payment_method=payment_method_id,
    currency='usd', amount=data['amount'] * 100, confirm=True)
    

     
    return Response(status=status.HTTP_200_OK, 
      data={
        'message': 'Success', 
        'data': {'customer_id': customer.id}   
      })                                   
