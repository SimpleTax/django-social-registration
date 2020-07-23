SAPO
======

- Add ``socialregistration.contrib.sapo`` to your ``INSTALLED_APPS``

::

	INSTALLED_APPS = (
		'socialregistration',
		'socialregistration.contrib.sapo'
	)


- Add ``socialregistration.contrib.sapo.auth.SapoAuth`` to your ``AUTHENTICATION_BACKENDS``

::

	AUTHENTICATION_BACKENDS = (
		'django.contrib.auth.backends.ModelBackend',
		'socialregistration.contrib.sapo.auth.SapoAuth',
	)

- Add your API keys:

::

	SAPO_CONSUMER_KEY = ''
	SAPO_CONSUMER_SECRET_KEY = ''


- Anywhere in your templates:

::

	{% load sapo %}
	{% sapo_button %}

Or:

::

	{% load sapo %}
	{% sapo_button 'custom/button/image.png' %}
