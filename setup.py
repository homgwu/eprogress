# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

import eprogress

setup(
    name="eprogress",
    version=eprogress.__version__,
    packages=find_packages(),
    author="HomgWu",
    author_email="homgwu@gmail.com",
    description="A simple and easy to use module for Python3 to print multi and single line progress bar in terminal",
    license='Apache-2.0',
    keywords=('multi line progress', 'progress bar', 'progress'),
    url="https://github.com/homgwu/eprogress.git",
)
