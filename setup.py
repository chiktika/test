from setuptools import setup, find_packages

setup(
    name='test',
    version='0.1.1',
    packages=find_packages(include=['test', 'test.*'])
)
