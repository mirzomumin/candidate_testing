from django.contrib.auth.backends import ModelBackend

from .models import CustomUser


class CustomBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = CustomUser.objects.get(email=email)
            if user.check_password(password) is True:
                return user
        except CustomUser.DoesNotExist:
            pass