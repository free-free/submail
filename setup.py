# coding:utf-8
from setuptools import setup,find_packages
import re

setup(
    name="submail",
    version="0.1",
    author="HuangBiao",
    author_email="19941222hb@gmail.com",
    description="submail sdk",
    license="MIT",
    package=find_packages(),
    install_requires=re.split(r"\r*\n+", open("requirements.txt", 'r').read())[0:-1],
    include_package_data=True
)
