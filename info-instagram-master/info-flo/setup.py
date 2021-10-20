# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='toutatis',
    version="1.0",
    packages=find_packages(),
    author="megadose",
    install_requires=["quidam"],
    description="Toutatis is a tool that allows you to extract information from instagrams accounts such as e-mails, phone numbers and more",
    long_description="",
    include_package_data=True,
    url='http://github.com/megadose/toutatis',
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
