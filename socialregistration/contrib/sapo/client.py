from django.conf import settings
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from socialregistration.clients.oauth import OAuth
from socialregistration.settings import SESSION_KEY
import json
import urlparse

class Sapo(OAuth):
    api_key = getattr(settings, 'SAPO_CONSUMER_KEY', '')
    secret_key = getattr(settings, 'SAPO_CONSUMER_SECRET_KEY', '')
    fixed_domain = getattr(settings,'SAPO_FIXED_DOMAIN',None)
    
    request_token_url = 'https://id.sapo.pt/oauth/request_token'
    access_token_url = 'https://id.sapo.pt/oauth/access_token'
    auth_url = 'https://id.sapo.pt/oauth/authorize'
    authentication_url = 'https://id.sapo.pt/oauth/authenticate'
    
    def get_callback_url(self):
        domain = self.fixed_domain
        if domain is None:
            domain = Site.objects.get_current().domain
            
        if self.is_https():
            return urlparse.urljoin(
                'https://%s' % domain,
                reverse('socialregistration:sapo:callback'))
        return urlparse.urljoin(
            'http://%s' % domain,
            reverse('socialregistration:sapo:callback'))

    def get_user_info(self):
        if self._user_info is None:
            profile_response = self.request('https://services.sapo.pt/SSO/GetBasicProfile')
            self._user_info = json.loads(profile_response)['GetBasicProfileResponse']['GetBasicProfileResult']['result']
            
        return self._user_info
    
    @staticmethod
    def get_session_key():
        return '%ssapo' % SESSION_KEY


