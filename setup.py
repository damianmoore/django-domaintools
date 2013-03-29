import os
from setuptools import setup

setup(
    name = "domaintools",
    version = "0.0.1",
    author = "Damian Moore",
    author_email = "django-domaintools@epixstudios.co.uk",
    description = ("Some tools for dealing with domain names"),
    license = "BSD",
    keywords = "django domain",
    url = "https://github.com/damianmoore/django-domaintools",
    packages=[
        'domaintools',
        'domaintools.migrations',
    ],
)
