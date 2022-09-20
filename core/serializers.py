from rest_framework.serializers import ModelSerializer
from rest_framework.authtoken.models import Token

from .models import Profile

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'username','password' ,'first_name',  'last_name', 'email', 'phone_number', 'address', 'role', 'department', 'is_admin', 'is_customer', 'is_employee', 'is_staff', 'is_active', 'date_joined']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile = Profile.objects.create_user(**validated_data)
        Token.objects.create(user=profile)
        return profile
# class UserSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'password')
#         # extra_kwargs = {'password': {'write_only': True, 'required': True}}
#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         Token.objects.create(user=user)
#         return user