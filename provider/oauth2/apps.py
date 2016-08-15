from __future__ import unicode_literals

from django.apps import AppConfig


class OAuth2Config(AppConfig):
    verbose_name = 'Provider OAuth2'
    name = 'provider.oauth2'
    label = 'oauth2'
