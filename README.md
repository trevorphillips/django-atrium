# django-atrium
An MX Atrium wrapper to be used with Django.

**This is a work in progress**

# Set up

1. In your settings file for your Django project, set these three variables **MX_API_KEY**, **MX_CLIENT_ID**, **MX_ATRIUM_URL**.
2. `from django_atrium import AtriumClient`
3. e.g. `AtriumClient().list_users()`
