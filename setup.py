#!/usr/bin/env python
"""
Facio
=====

Facio is a project scaffolding tool origionally developed for Django
and expanded to be framework agnostic. You can use facio to bootstrap
any sort of project.
"""

from facio import __version__
from setuptools import setup, find_packages


install_requires = ['GitPython==0.3.2.RC1', 'Jinja2==2.6']

setup(
    name='facio',
    version=__version__,
    author='Christopher John Reeves',
    author_email='hello@chris.reeves.io',
    url='http://chris.reeves.io',
    description='Project scaffolding from custom templates.',
    long_description=__doc__,
    zip_safe=False,
    packages=find_packages(exclude=['tests', ]),
    install_requires=install_requires,
    scripts=['facio/bin/facio'],
    package_data={'': [
        'default_template/index.html',
        'default_template/css/bootstrap.css',
    ]},
    classifiers=[
        'Environment :: Console',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Developers',
        'Operating System :: Unix',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
