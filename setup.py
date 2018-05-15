#!/usr/bin/env python

from __future__ import print_function

from setuptools import setup, find_packages

entry_points = """
[glue.plugins]
myplugin=myplugin:setup
"""

with open('README.rst') as infile:
    LONG_DESCRIPTION = infile.read()

with open('myplugin/version.py') as infile:
    exec(infile.read())

setup(name='myplugin',
      version=__version__,
      description='My example plugin',
      long_description=LONG_DESCRIPTION,
      url="https://github.com/glue-viz/glue-plugin-template",
      author='',
      author_email='',
      packages = find_packages(),
      package_data={},
      entry_points=entry_points
    )
