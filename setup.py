#!/usr/bin/env python
# -*- coding: utf-8 -*-
import setuptools
import unittest

# Read the contents of the README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(name='hyper2rgb',
    version='0.1.0',
    description='Python module to convert hyperspectral images to RGB.',
    author='Luis C. Garcia-Peraza Herrera',
    author_email='luiscarlos.gph@gmail.com',
    license='MIT License',
    url='https://github.com/luiscarlosgph/hyper2rgb',
    packages=[
        'hyper2rgb',
    ],
    package_dir={
        'hyper2rgb': 'src',
    },
    install_requires = [
        'numpy', 
        'opencv-python',
        'matplotlib',
        'seaborn',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    test_suite = 'test',
)
