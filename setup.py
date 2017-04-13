from setuptools import setup, find_packages


setup(
    name="SimpleES",
    version="0.10.0",
    description='A simple Event Sourcing library for Python',
    packages=find_packages('src'),
    package_dir={'': 'src'}
)
