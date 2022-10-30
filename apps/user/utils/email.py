from django.core.mail import EmailMessage
from django.conf import settings

from user.models import CustomUser


def send_confirm_mail(user_id):
	'''Send message for email verification'''
	user = CustomUser.objects.get(id=user_id)
	url = f'{settings.BACKEND_DOMAIN}api/v1/user/confirm/?confirmation-code={user.confirmation_code}'
	message = f'Confirm email by clicking on link below:\n\n\
		{url}\
		\n\nThank you for verification!'
	email = EmailMessage(
		'Email Confirmation',
		message,
		settings.EMAIL_HOST_USER,
		(user.email,),
	)
	email.send()


def send_reset_password_email(email):
	'''Send email to reset password'''
	user = CustomUser.objects.get(email=email)
	url = f'{settings.BACKEND_DOMAIN}api/v1/user/password-reset/complete/?user_id={user.id}'
	message = f'Reset password by clicking on the link below:\n\n\
		{url}\
		\n\nThanks for reseting password!'
	email = EmailMessage(
		'Reset Password',
		message,
		settings.EMAIL_HOST_USER,
		(email,),
	)
	email.send()