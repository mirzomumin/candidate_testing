from rest_framework.decorators import api_view
from rest_framework.status import (
	HTTP_400_BAD_REQUEST,
	HTTP_200_OK)
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema


from user.serializers.reset_password import (
	ResetPasswordEmailSerializer,
	ResetPasswordSerializer)
from user.utils.email import send_reset_password_email
from user.models import CustomUser


@swagger_auto_schema(method='post', request_body=ResetPasswordEmailSerializer)
@api_view(['POST'])
def send_reset_password_instruction(request):
	'''Send instruction to reset user password'''
	serializer = ResetPasswordEmailSerializer(data=request.data)
	if serializer.is_valid(raise_exception=True):
		send_reset_password_email(serializer.data['email'])
		return Response({'response': 'Success!'},
			status=HTTP_200_OK)
	return Response({'Bad Request!'},
		status=HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='patch', request_body=ResetPasswordSerializer)
@api_view(['PATCH'])
def reset_password(request):
	'''Reset user password'''
	user_id = request.query_params.get('user_id')
	if user_id is not None:
		serializer = ResetPasswordSerializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			user = CustomUser.objects.get(id=user_id)
			if user is not None:
				user.set_password(serializer.data['password'])
				user.save()
				return Response({'response': 'Successfully reset password!'},
					status=HTTP_200_OK)
		return Response({'response': 'Bad Request!'},
			status=HTTP_400_BAD_REQUEST)
	return Response({'response': 'User ID or token is not valid!'},
		status=HTTP_400_BAD_REQUEST)