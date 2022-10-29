from rest_framework import serializers

from user.models import CustomUser


class SignUpSerializer(serializers.ModelSerializer):
	password = serializers.CharField(max_length=68, min_length=6, write_only=True)
	class Meta:
		model = CustomUser
		fields = ('username', 'last_name', 'email', 'phone', 'password')