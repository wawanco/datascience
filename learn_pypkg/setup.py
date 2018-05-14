#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name='learn_pypkg',
    version='0.1dev',
    packages=find_packages(exclude=('tests',)),
    install_requires=['numpy'],
    entry_points={
        'console_scripts': [
            'learn_pypkg = learn_pypkg.__main__:main',
        ],
    }
)
