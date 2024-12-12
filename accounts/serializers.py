from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'firstName','is_active', 'is_staff']  # Specify fields to include in the API
