from django.conf import settings
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt

from .models import User, Users
import jwt
from django.utils.deprecation import MiddlewareMixin
from rest_framework import authentication, exceptions


class SettingRequest(MiddlewareMixin):
    authentication_header_prefix = 'Bearer token'
    def process_view(self, request, view, args, kwargs):
      auth_header = authentication.get_authorization_header(request).split()
      if auth_header:
        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')
        return self._authenticate_credentials(request, token)

    def _authenticate_credentials(self, request, token):
      payload = jwt.decode(token, settings.SECRET_KEY)
      user = Users.objects.get(username = payload['user'])
      print(user)
      request.role= payload['type'] or ""



