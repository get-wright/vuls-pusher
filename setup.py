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


#   hosts:
#     - "https://test-api-bb4c28.es.ap-southeast-1.aws.elastic.cloud:443"
#   api_key: "UnVraEdKU5SjtFQIDlrN6tS2kcnqlSvJ2ekd1UXF2ND.5c3FQ5npYZ=="