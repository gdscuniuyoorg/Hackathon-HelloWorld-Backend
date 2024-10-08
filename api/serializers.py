from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import CustomUser, Attendance


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password',
                  'first_name', 'last_name', 'phone_number', 'reg_no', 'role')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        # Ensure only students have reg_no
        if data.get('role') != 'student' and data.get('reg_no'):
            raise serializers.ValidationError({
                'reg_no': 'Only students can have registration numbers'
            })
        return data

    def create(self, validated_data):
        # Hash password before saving
        validated_data['password'] = make_password(validated_data['password'])
        return super(CustomUserSerializer, self).create(validated_data)


class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'phone_number', 'reg_no')


class AttendanceSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField()

    class Meta:
        model = Attendance
        fields = ['reg_no', 'time', 'course', 'date']

    def create(self, validated_data):
        return Attendance.objects.create(**validated_data)
