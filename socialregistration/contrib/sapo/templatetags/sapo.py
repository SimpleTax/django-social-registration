from django import template
from socialregistration.templatetags import button

register = template.Library()

register.tag('sapo_button', button('socialregistration/sapo/sapo_button.html'))
