# coding:utf-8

from setuptools import setup,find_packages
import re
import os

from submail import __version__


def read(f):
    return open(os.path.join(os.path.dirname(__file__),f)).read().strip()


setup(
    name="submail",
    version=__version__,
    author="HuangBiao",
    author_email="19941222hb@gmail.com",
    long_description=read('README.rst'),
    description="submail sdk",
    url="https://github.com/free-free/submail",
    license="MIT",
    packages=find_packages(),
    install_requires=re.split(r'\r*\n+',read('requirements.txt')),
    include_package_data=True,
    keywords=['submail','sdk'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
