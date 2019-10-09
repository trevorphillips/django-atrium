from setuptools import setup


def readme():
    with open('README.md') as f:
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

packages = ['django_atrium']

requires = ['atrium==2.8.0']

setup(name='django-atrium',
      version='0.2',
      description='An MX Atrium wrapper to be used with Django.',
      url='https://github.com/trevorphillips/django-atrium',
      author='Trevor Phillips',
      author_email='trevorcoreyphillips@gmail.com',
      license='GNU',
      classifiers=classifiers,
      packages=packages,
      install_requires=requires,
      zip_safe=False)
