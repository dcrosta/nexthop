#!/usr/bin/env python
from setuptools import setup

setup(name='nexthop',
      version='0.1.0',
      description='Simple HTTP redirection service',
      url='https://github.com/dcrosta/nexthop.git',
      py_modules=['nexthop'],
      install_requires=[l.strip() for l in file('requirements.txt').readlines() if l.strip() != ''],
     )
