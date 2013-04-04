#!/usr/bin/env python
from setuptools import setup


setup(
    name='flask-sqlalchemy-manager',
    version='0.0.1',
    description='Extesion for Flask with integration `sqlalchemy-manager`',
    long_description=open('README.rst').read(),
    author='Roman Gladkov',
    author_email='d1fffuz0r@gmail.com',
    url='https://github.com/d1ffuz0r/flask=sqlalchemy-manager',
    install_requires=['sqlalchemy', 'Flask'],
    py_modules=['flask_alchmanager'],
    zip_safe=False,
    test_suite='tests',
    classifiers=(
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
    )
)
