#! /usr/bin/env python
import sys

try:
    from setuptools import setup
    extra = {
        'install_requires': ['argparse']
    }
    if sys.version_info >= (3,):
        extra['use_2to3'] = True
except ImportError:
    from distutils.core import setup
    extra = {
        'dependencies': ['argparse']
    }

setup(name               = 'shovel-campfire',
    version              = '0.1.0',
    description          = 'Campfire client for shovel',
    url                  = 'http://github.com/seomoz/shovel-campfire',
    author               = 'Dan Lecocq',
    author_email         = 'dan@moz.com',
    license              = "MIT License",
    keywords             = 'tasks, shovel, rake, campfire',
    include_package_data = True,
    scripts              = ['bin/shovel-campfire'],
    classifiers          = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent'
    ],
    **extra
)
