from setuptools import setup, find_packages


setup(
    name="SimpleES",
    version="0.7.0",
    description='A simple Event Sourcing library for Python',
    packages=find_packages(),
    package_dir={'': '.'}
)
