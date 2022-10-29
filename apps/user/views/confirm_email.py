from rest_framework.decorators import api_view
from rest_framework.status import (
	HTTP_400_BAD_REQUEST,
	HTTP_200_OK)
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from drf_yasg.utils import swagger_auto_schema

from user.serializers.confirm_email import ConfirmationCodeSerializer
from user.models import CustomUser


@swagger_auto_schema(method='get', query_serializer=ConfirmationCodeSerializer)
@api_view(['GET'])
def confirm(request):
	'''Confirm signed up user email'''
	code = request.query_params.get('confirmation-code')
	if code is not None:
		data = {'confirmation_code': code}
		serializer = ConfirmationCodeSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			code = serializer.data['confirmation_code']
			user = get_object_or_404(
				CustomUser,
				confirmation_code=code,
				verified_at=None,
				is_active=False)
			user.verified_at = now()
			user.is_active = True
			user.save()
			return Response({'response': 'Successfully Verified!'},
				status=HTTP_200_OK)
	return Response({'response': 'Bad Request'},
		status=HTTP_400_BAD_REQUEST)