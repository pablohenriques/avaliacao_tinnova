from setuptools import setup, find_packages


setup(
    name='api',
    version='0.1.0',
    packages=find_packages(include=['api', 'api.*']),
    include_package_data=True
)
