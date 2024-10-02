from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import CustomUser
# from django.contrib.auth.models import User


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password',
                  'first_name', 'last_name', 'phone_number', 'reg_no', 'role')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        # Hash password before saving
        validated_data['password'] = make_password(validated_data['password'])
        return super(CustomUserSerializer, self).create(validated_data)
