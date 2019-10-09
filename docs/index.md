# django-atrium [![Build Status](https://travis-ci.com/trevorphillips/django-atrium.svg?branch=master)](https://travis-ci.com/trevorphillips/django-atrium)
An MX Atrium wrapper to be used with Django.

Documentation can be found [here](https://github.com/trevorphillips/django-atrium/tree/master/docs/django_atrium).

1. In your settings file for your Django project, set these three variables:
- **MX_API_KEY**
- **MX_CLIENT_ID**
- **MX_ATRIUM_URL**.
2. import using `from django_atrium import AtriumClient` from any file.
3. That's it!
