# See LICENSE.incore for details

"""The setup script."""
import os
from setuptools import setup, find_packages

# Base directory of package
here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()

def read_requires():
    with open(os.path.join(here, "webtree/requirements.txt"),"r") as reqfile:
        return reqfile.read().splitlines()

#Long Description
with open("README.md", "r") as fh:
    long_description = fh.read()

setup_requirements = [ ]

test_requirements = [ ]

setup(
    name='webtree',
    version='0.0.1',
    description="Displays HTML page as a Graph",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url='https://github.com/abishekshyamsunder/webtree',
    author="Abishek Shyamsunder, Adithya Viswanathan",
    author_email='abishekshyamsunder@gmail.com',
    license="MIT license",
    packages=find_packages(),
    package_dir={'webtree': 'webtree'},
    install_requires=read_requires(),
    python_requires='>=3.6.0',
    entry_points={
        'console_scripts': ['webtree=webtree.main:cli'],
    },
    include_package_data=True,
    keywords='webtree',
    zip_safe=False,
)