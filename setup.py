from setuptools import setup, find_packages

setup(
    name='vuls_elk_ingestor',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'elasticsearch',
        'python-dateutil',
        'pyyaml',
    ],
)