from setuptools import setup, find_packages


setup(
    name="simple-es",
    version="0.12.1",
    description='A simple Event Sourcing library for Python',
    packages=find_packages('src'),
    package_dir={'': 'src'}
)
