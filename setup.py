from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


classifiers = [
    "Natural Language :: English",
    "Development Status :: 5 - Production/Stable",
    "Environment :: Web Environment",
    "Framework :: Django",
    "Intended Audience :: Developers",
    "Programming Language :: Python",
    "Topic :: Utilities",
]

packages = ['django_atrium']

requires = ['atrium==2.8.0', 'python-dotenv==0.10.3']

setup(name='django-atrium',
      version='1.2.1,
      description='An MX Atrium wrapper to be used with Django.',
      url='https://github.com/trevorphillips/django-atrium',
      author='Trevor Phillips',
      author_email='trevorcoreyphillips@gmail.com',
      license='GNU',
      classifiers=classifiers,
      packages=packages,
      install_requires=requires,
      download_url=
      'https://github.com/trevorphillips/django-atrium/archive/v1.2.1.tar.gz',
      zip_safe=False)
