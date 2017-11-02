# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='glacierclient',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': 'glacierclient = glacierclient.main:main'
    },
    data_files=[('/usr/local/etc', ['glacier.conf'])],
    zip_safe=False,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)
