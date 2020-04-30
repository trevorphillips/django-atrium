# django-atrium

![django-atrium tests](https://github.com/trevorphillips/django-atrium/workflows/django-atrium%20tests/badge.svg) [![codecov](https://codecov.io/gh/trevorphillips/django-atrium/branch/master/graph/badge.svg)](https://codecov.io/gh/trevorphillips/django-atrium)

A high-level MX Atrium wrapper to be used with Django.

Documentation can be found [here](https://trevorphillips.github.io/django-atrium/index.html).

1. Add `django_atrium` to your `INSTALLED_APPS` settings file.

2. In your settings file for your Django project, set these three variables:

- **ATRIUM_API_KEY**
- **ATRIUM_CLIENT_ID**
- **ATRIUM_URL**

3. import using `from django_atrium import AtriumClient` from any file.

## Formatting

`black .`

## Documentation

`pdoc ./django_atrium  --html -o docs/`
