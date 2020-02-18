from setuptools import find_packages, setup


def read(f):
    return open(f, "r", encoding="utf-8").read()


classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Web Environment",
    "Framework :: Django",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "Programming Language :: Python",
    "Topic :: Utilities",
]

requires = ["atrium==2.8.0", "django>=1.11"]

setup(
    author="Trevor Phillips",
    author_email="trevorcoreyphillips@gmail.com",
    classifiers=classifiers,
    description="An MX Atrium wrapper to be used with Django.",
    install_requires=requires,
    license="MIT",
    long_description=read("README.md"),
    name="django-atrium",
    packages=find_packages(exclude=["tests*"]),
    url="https://github.com/trevorphillips/django-atrium",
    version="2.0.1",
    zip_safe=False,
)
