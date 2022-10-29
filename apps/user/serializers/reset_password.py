from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from user.models import CustomUser


class ResetPasswordEmailSerializer(serializers.Serializer):
	email = serializers.EmailField(required=True)
	class Meta:
		model = CustomUser
		fields = ('email',)

	def validate(self, attrs):
		email = attrs.get('email','')
		user = CustomUser.objects.get(email=email)
		if not user:
			raise AuthenticationFailed('User with this email doesn\'t exist!')
		if not user.is_active:
			raise AuthenticationFailed('Account disabled, contact admin')
		return {
			'email': email,
		}


class ResetPasswordSerializer(serializers.Serializer):
	password = serializers.CharField(min_length=6, max_length=68,
		required=True)