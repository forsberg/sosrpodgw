#!/usr/bin/env python

from setuptools import setup, find_packages

print find_packages()

setup(name='So SR POD Gateway',
      version='1.0',
      description='Web Gateway for listing all PODcasts from Sveriges Radio and play them on Sonos',
      author='Erik Forsberg',
      author_email='forsberg@efod.se',
      packages=find_packages(),
      install_requires=['soco', "Flask==0.10.1", "Flask-bootstrap", "Flask-appconfig"],
      zip_safe=False,
     )
