from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.shortcuts import get_object_or_404

from user.models import CustomUser


class SignInSerializer(serializers.Serializer):
	password = serializers.CharField(max_length=68,
		min_length=6, write_only=True)
	email = serializers.EmailField(required=True)
	tokens = serializers.SerializerMethodField(read_only=True)
	username = serializers.SerializerMethodField(read_only=True)
	last_name = serializers.SerializerMethodField(read_only=True)
	phone = serializers.SerializerMethodField(read_only=True)
	class Meta:
		model = CustomUser
		fields = ('username', 'last_name', 'email', 'tokens', 'password')

	def get_tokens(self, obj):
		user = get_object_or_404(CustomUser, email=obj['email'])
		return {
			'refresh': user.tokens()['refresh'],
			'access': user.tokens()['access']
		}

	def get_username(self, obj):
		user = get_object_or_404(CustomUser, email=obj['email'])
		if user.username is not None:
			return user.username

	def get_last_name(self, obj):
		user = get_object_or_404(CustomUser, email=obj['email'])
		if user.last_name is not None:
			return user.last_name

	def get_phone(self, obj):
		user = get_object_or_404(CustomUser, email=obj['email'])
		if user.phone is not None:
			return str(user.phone)

	def validate(self, attrs):
		email = attrs.get('email','')
		password = attrs.get('password','')
		user = authenticate(email=email, password=password)
		if not user:
			raise AuthenticationFailed('Invalid credentials, try again')
		if not user.is_active:
			raise AuthenticationFailed('Account disabled, contact admin')
		return {
			'email': user.email,
			'tokens': user.tokens,
			'phone': user.phone,
			'username': user.username,
			'last_name': user.last_name,
		}