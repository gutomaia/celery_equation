# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from os import path


here = path.abspath(path.dirname(__file__))


setup(
    name='equation',
    version='0.0.1',
    description='equation',
    author="Guto Maia",
    author_email="guto@guto.net",
    license="Mit",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "wednesday"]),
    classifiers=[
        'Development Status :: 3 - Alpha',
    ]
)
