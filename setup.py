from setuptools import setup, find_packages


setup(
    name="SimpleES",
    version="0.1.0",
    description='A simple Event Sourcing library for Python',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    setup_requires=['pytest-runner=2.9'],
    tests_require=['pytest==2.9.2']
)
