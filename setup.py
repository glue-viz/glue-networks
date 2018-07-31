#!/usr/bin/env python

from __future__ import print_function

from setuptools import setup, find_packages

entry_points = """
[glue.plugins]
glue_networks=glue_networks:setup
"""

with open('README.rst') as infile:
    LONG_DESCRIPTION = infile.read()

with open('glue_networks/version.py') as infile:
    exec(infile.read())

setup(name='glue-networks',
      version=__version__,
      description='Plugin for glue to visualize network data',
      long_description=LONG_DESCRIPTION,
      url="https://github.com/chaityacshah/glue-networks",
      author='',
      author_email='',
      packages = find_packages(),
      package_data={'glue_networks.tests':['data/*']},
      entry_points=entry_points,
      install_requires=['glue-core>=0.12']
    )
