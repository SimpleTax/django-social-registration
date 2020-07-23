from django.contrib.auth.backends import ModelBackend
from django.contrib.sites.models import Site
from socialregistration.contrib.sapo.models import SapoProfile


class SapoAuth(ModelBackend):
    def authenticate(self, sapo=None):
        try:
            return SapoProfile.objects.get(
                sapo=sapo,
                site=Site.objects.get_current()
            ).user
        except SapoProfile.DoesNotExist:
            return None
