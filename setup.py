import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "twc_square",
    version = "0.1.9",
    author = "Sabbir Rashid",
    author_email = "rashidsabbir@gmail.com",
    description = ("The twc_square package contains configuration entries for SQuARE, the SPARQL Query Agent-based Reasoning Engine"),
    license = "Apache License 2.0",
    keywords = "rdf semantic inference reasoning engine",
    url = "http://packages.python.org/twc_square",
    packages=find_packages(),
    long_description='''The twc_square package contains configuration entries for SQuARE, the SPARQL Query Agent-based Reasoning Engine.''',
    include_package_data = False,
    install_requires = [],
    entry_points = {
        'console_scripts': ['twc_square=twc_square:main'],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License",
    ],
)
