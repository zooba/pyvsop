from setuptools import setup, find_packages
from pathlib import Path

here = Path(__file__).parent

# Get the long description from the relevant file
with open(str(here /'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyvsop',
    version='0.1',

    description='A sample Python project',
    long_description=long_description,
    url='https://github.com/zooba/pyvsop',

    # Author details
    author='Steve Dower',
    author_email='steve.dower@microsoft.com',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='planets vsop',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[],
    package_data={
        'vsop.vsop87': ['VSOP87*'],
    },
)

