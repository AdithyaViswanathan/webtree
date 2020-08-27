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
#     with open(os.path.join(here, "aapg/requirements.txt"),"r") as reqfile:
#         return reqfile.read().splitlines()

#Long Description
# with open("README.rst", "r") as fh:
#     readme = fh.read()

setup_requirements = [ ]

test_requirements = [ ]

setup(
    name='webtree',
    version='1.0',
    description="RISC-V AAPG",
    # long_description=readme + '\n\n',
    classifiers=[
          "Programming Language :: Python :: 3.6",
          "License :: OSI Approved :: BSD License",
          "Development Status :: 4 - Beta"
    ],
    # url='https://gitlab.com/lavanyajagan/aapg',
    # author="InCore Semiconductors Pvt. Ltd.",
    # author_email='incorebot@gmail.com',
    # license="MIT license",
    packages=find_packages(),
    package_dir={'webtree': 'webtree'},
    # install_requires=read_requires(),
    python_requires='>=3.6.0',
    entry_points={
        'console_scripts': ['webtree=webtree.main:cli'],
    },
    include_package_data=True,
    keywords='webtree',
    #test_suite='tests',
    #tests_require=test_requirements,
    zip_safe=False,
)