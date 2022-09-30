from django.shortcuts import render
from .serializers import ProfileSerializer

from .models import Profile
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view,  permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.http import JsonResponse

# Create your views here.

def welcome(request):
    return JsonResponse({'message': 'Welcome to the backend'})

class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    http_method_names = ['post']


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_my_details(request):
    user_id = Token.objects.get(key=request.auth).user_id
    orders = Profile.objects.filter(id=user_id)
    serializer = ProfileSerializer(orders, many=True)
    return Response(serializer.data)

