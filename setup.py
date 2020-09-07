# See LICENSE.incore for details

"""The setup script."""
import os
from setuptools import setup, find_packages

# Base directory of package
here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()

# def read_requires():
#     with open(os.path.join(here, "requirements.txt"),"r") as reqfile:
#         install_requires = list(reqfile.read().splitlines())
#     return install_requires

#Long Description
with open("README.md", "r") as fh:
    long_description = fh.read()

setup_requirements = [ ]

test_requirements = [ ]

setup(
    name='webtree',
    version='0.0.17',
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
    author_email='abishekshyamsunder@gmail.com, adith_viswa@ymail.com',
    license="MIT license",
    packages=find_packages(),
    package_dir={'webtree': 'webtree'},
    install_requires=['dash>=1.14.0', 'dash-core-components>=1.10.2', 'dash-html-components>=1.0.3', 'plotly>=4.9.0', 'networkx>=2.4', 'matplotlib>=3.2.1', 'pandas>=1.0.3', 'beautifulsoup4>=4.9.1', 'chart-studio>=1.1.0', 'requests>=2.22.0', 'Click>=7.0', 'lxml>=4.5.2', 'scipy>=1.5.2',],
    python_requires='>=3.6.0',
    entry_points={
        'console_scripts': ['webtree=webtree.main:cli'],
    },
    include_package_data=True,
    keywords='webtree',
    zip_safe=False,
)