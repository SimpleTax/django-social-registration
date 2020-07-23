from django.core.urlresolvers import reverse
from socialregistration.contrib.sapo.client import Sapo
from socialregistration.contrib.sapo.models import SapoProfile
from socialregistration.views import OAuthRedirect, OAuthCallback, SetupCallback

class SapoRedirect(OAuthRedirect):
    client = Sapo
    template_name = 'socialregistration/sapo/sapo.html'

class SapoCallback(OAuthCallback):
    client = Sapo
    template_name = 'socialregistration/sapo/sapo.html'
    
    def get_redirect(self):
        return reverse('socialregistration:sapo:setup')

class SapoSetup(SetupCallback):
    client = Sapo
    profile = SapoProfile
    template_name = 'socialregistration/sapo/sapo.html'
    
    def get_lookup_kwargs(self, request, client):
        #use Sapo primary id as key
        return {'sapo': client.get_user_info()['userid']}
    
