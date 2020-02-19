# django-atrium

![django-atrium tests](https://github.com/trevorphillips/django-atrium/workflows/django-atrium%20tests/badge.svg)

An MX Atrium wrapper to be used with Django.

Documentation can be found [here](https://trevorphillips.github.io/django-atrium/index.html).

1.  In your settings file for your Django project, set these three variables:

-   **ATRIUM_API_KEY**
-   **ATRIUM_CLIENT_ID**
-   **ATRIUM_URL**.

2.  import using `from django_atrium import AtriumClient` from any file.
3.  That's it!

## Formatting

`black .`

## Documentation

`pdoc ./django_atrium  --html -o docs/`
