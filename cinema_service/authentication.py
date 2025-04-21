from django.contrib.auth import get_user_model
from rest_framework import authentication

class AlwaysAuth(authentication.BaseAuthentication):
    def authenticate(self, request):
        user = get_user_model().objects.get(username="admin.user")
        return (user, None)
