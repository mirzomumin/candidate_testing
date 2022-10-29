from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import (
	HTTP_400_BAD_REQUEST,
	HTTP_200_OK)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from user.serializers.change_password import ChangePasswordSerializer


@swagger_auto_schema(method='post', request_body=ChangePasswordSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
	'''Change old password to new password'''
	serializer = ChangePasswordSerializer(data=request.data)
	if serializer.is_valid(raise_exception=True):
		user = request.user
		if user.check_password(serializer.data['old_password']) is True:
			user.set_password(serializer.data['new_password'])
			user.save()
			return Response({'response': 'Successfully changed password!'},
				status=HTTP_200_OK)
		return Response({'response': 'Invalid current old password!'},
			status=HTTP_400_BAD_REQUEST)
	return Response({'response': 'Invalid data!'},
		status=HTTP_400_BAD_REQUEST)