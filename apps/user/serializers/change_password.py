from rest_framework import serializers

from django.shortcuts import get_object_or_404

from user.models import CustomUser


class ChangePasswordSerializer(serializers.Serializer):
	'''Necessary information for changing password'''
	old_password = serializers.CharField(min_length=6,
		max_length=68)
	new_password = serializers.CharField(min_length=6,
		max_length=68)