# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os
from setuptools import setup, find_packages

version = '0.2.1'

# get documentation from the README
try:
    here = os.path.dirname(os.path.abspath(__file__))
    description = file(os.path.join(here, 'README.md')).read()
except (OSError, IOError):
    description = ''

# dependencies
deps = ['datazilla>=1.2',
        'marionette_client>=0.5.20']

setup(name='microbench',
      version=version,
      description="Microbench POC",
      long_description=description,
      classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='mozilla',
      author='Mozilla Automation and Testing Team',
      author_email='tools@lists.mozilla.org',
      url='https://github.com/ctalbert/microbench',
      license='MPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      package_data={},
      include_package_data=True,
      zip_safe=False,
      entry_points="""
      [console_scripts]
      microbench = microbench.benchtestrunner:main
      """,
      install_requires=deps,
      )