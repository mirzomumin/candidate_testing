from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework_simplejwt.tokens import RefreshToken
import uuid
# Create your models here.

class CustomUser(AbstractUser):
	'''Customized User for E-commerce project'''
	username = models.CharField('first_name', max_length=128, unique=False)
	last_name = models.CharField('last_name', max_length=128)
	email = models.EmailField(blank=False, null=False, unique=True)
	phone = PhoneNumberField(blank=True, null=True, unique=True)
	confirmation_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=True)
	verified_at = models.DateTimeField(null=True, blank=True)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username', 'last_name']

	def tokens(self):
		'''Return access and refresh tokens'''
		refresh = RefreshToken.for_user(self)
		return{
			'refresh':str(refresh),
			'access':str(refresh.access_token)
		}