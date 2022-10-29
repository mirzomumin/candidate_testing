from rest_framework.decorators import api_view
from rest_framework.status import (
	HTTP_400_BAD_REQUEST,
	HTTP_200_OK)
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from user.serializers.sign_in import SignInSerializer


@swagger_auto_schema(method='post', request_body=SignInSerializer)
@api_view(['POST'])
def sign_in(request):
	'''Sign in user to app'''
	serializer = SignInSerializer(data=request.data)
	if serializer.is_valid(raise_exception=True):
		return Response({'response': 'Success!',
			'data': serializer.data},
			status=HTTP_200_OK)
	return Response({'response': 'Bad Request!'},
		status=HTTP_400_BAD_REQUEST)