from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import (
	HTTP_400_BAD_REQUEST,
	HTTP_204_NO_CONTENT)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from user.serializers.sign_out import SignOutSerializer


@swagger_auto_schema(method='post', request_body=SignOutSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def sign_out(request):
	'''Sign Out user through refresh token'''
	serializer = SignOutSerializer(data=request.data)
	if serializer.is_valid(raise_exception=True):
		serializer.save()
		return Response({'response': 'Successfully signed out!'},
			status=HTTP_204_NO_CONTENT)
	return Response({'response': 'Error'}, status=HTTP_400_BAD_REQUEST)