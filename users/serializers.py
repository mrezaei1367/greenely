from rest_framework.serializers import ModelSerializer
from .models import User


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id"
            "username",
            'address',
            'mobile_number',
            'first_name',
            'last_name'
        ]
