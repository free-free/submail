# coding:utf-8

from setuptools import setup,find_packages
import re
from submail import __version__

setup(
    name="submail",
    version=__version__,
    author="HuangBiao",
    author_email="19941222hb@gmail.com",
    description="submail sdk",
    url="https://github.com/free-free/submail",
    license="MIT",
    packages=find_packages(),
    install_requires=re.split(r"\r*\n+", open("requirements.txt", 'r').read())[0:-1],
    include_package_data=True,
    keywords=['submail','sdk'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
