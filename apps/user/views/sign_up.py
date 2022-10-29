from rest_framework.decorators import api_view
from rest_framework.status import (
	HTTP_400_BAD_REQUEST,
	HTTP_201_CREATED)
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from user.serializers.sign_up import SignUpSerializer
from user.utils.email import send_confirm_mail


@swagger_auto_schema(method='post', request_body=SignUpSerializer)
@api_view(['POST'])
def sign_up(request):
	'''Sign up user to app'''
	serializer = SignUpSerializer(data=request.data)
	if serializer.is_valid(raise_exception=True):
		user = serializer.save()
		user.set_password(user.password)
		user.is_active = False
		user.save()
		send_confirm_mail(user.id)
		return Response({'response': 'Successfully signed up!'},
			status=HTTP_201_CREATED)
	return Response({'response': 'Bad Request!'},
		status=HTTP_400_BAD_REQUEST)