from setuptools import setup

setup(name='django-atrium',
      version='0.1',
      description='An MX Atrium wrapper to be used with Django.',
      url='https://github.com/trevorphillips/django-atrium',
      author='Trevor Phillips',
      license='GNU',
      packages=['django_atrium'],
      install_requires=[
          'requests',
          'atrium',
      ],
      zip_safe=False)
