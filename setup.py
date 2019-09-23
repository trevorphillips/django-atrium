from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


classifiers = [
    "Natural Language :: English",
    "Development Status :: 5 - Production/Stable",
    "Environment :: Web Environment",
    "Framework :: Django",
    "Framework :: Django :: 1.11",
    "Framework :: Django :: 2.0",
    "Framework :: Django :: 2.1",
    "Intended Audience :: Developers",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Topic :: Utilities",
]

install_requires = [
    'requests',
    'atrium',
]

setup(name='django-atrium',
      version='0.1',
      description='An MX Atrium wrapper to be used with Django.',
      url='https://github.com/trevorphillips/django-atrium',
      author='Trevor Phillips',
      license='GNU',
      classifiers=classifiers,
      packages=['django_atrium'],
      install_requires=install_requires,
      zip_safe=False)
