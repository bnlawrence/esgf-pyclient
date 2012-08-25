# BSD Licence
# Copyright (c) 2012, Science & Technology Facilities Council (STFC)
# All rights reserved.
#
# See the LICENSE file in the source distribution of this software for
# the full license text.

from setuptools import setup, find_packages
import sys, os

# Import version from the top-level package
sys.path[:0] = os.path.dirname(__file__)
from esgf_search import __version__
from esgf_search import __doc__ as long_description

setup(name='esgf_search_client',
      version=__version__,
      description="A library querying the ESGF search API",
      long_description=long_description,
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Stephen Pascoe',
      author_email='Stephen.Pascoe@stfc.ac.uk',
      url='http://github.org/stephenpascoe/esgf-search-client',
      #download_url='',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'test']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
      ],
      #tests_require=['NoseXUnit'],
      entry_points= {
        },
      test_suite='nose.collector',
      )
