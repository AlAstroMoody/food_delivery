from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=6,
        write_only=True,
    )

    class Meta:
        model = User
        fields = 'username', 'password', 'email'

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
