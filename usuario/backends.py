from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EmailBackend(ModelBackend):
    def authenticate(self, request, username = None, password = None, **kwargs):
        User = get_user_model()
        try:
            account = User.objects.get(email = username)
        except User.DoesNotExist:
            return None
        else:
            if account.check_password(password):
                return account
        return None