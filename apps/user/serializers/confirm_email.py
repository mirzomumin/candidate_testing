from rest_framework import serializers

class ConfirmationCodeSerializer(serializers.Serializer):
	'''Confirmation code'''
	confirmation_code = serializers.CharField(max_length=128)