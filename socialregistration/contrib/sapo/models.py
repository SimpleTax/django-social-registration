from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.db import models
from socialregistration.signals import connect

class SapoProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    site = models.ForeignKey(Site, default=Site.objects.get_current)
    sapo = models.CharField(max_length=100)

    def __unicode__(self):
        try:
            return u'%s: %s' % (self.user, self.sapo)
        except User.DoesNotExist:
            return u'None'

    def authenticate(self):
        return authenticate(sapo=self.sapo)

class SapoRequestToken(models.Model):
    profile = models.OneToOneField(SapoProfile, related_name='request_token')
    oauth_token = models.CharField(max_length=512)
    oauth_token_secret = models.CharField(max_length=80)

class SapoAccessToken(models.Model):
    profile = models.OneToOneField(SapoProfile, related_name='access_token')
    oauth_token = models.CharField(max_length=512)
    oauth_token_secret = models.CharField(max_length=80)

def save_sapo_token(sender, user, profile, client, **kwargs):
    try:
        SapoRequestToken.objects.get(profile=profile).delete()
    except SapoRequestToken.DoesNotExist:
        pass
    try:
        SapoAccessToken.objects.get(profile=profile).delete()
    except SapoAccessToken.DoesNotExist:
        pass
    
    SapoRequestToken.objects.create(profile=profile,
        oauth_token=client.get_request_token().key,
        oauth_token_secret=client.get_request_token().secret)
    
    SapoAccessToken.objects.create(profile=profile,
        oauth_token=client.get_access_token().key,
        oauth_token_secret=client.get_access_token().secret)

connect.connect(save_sapo_token, sender=SapoProfile,
    dispatch_uid='socialregistration_sapo_token')
