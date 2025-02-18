from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from elasticsearch import ConnectionError, ConnectionTimeout
from datetime import datetime
from time import sleep
import logging

def retry_on_connection_error(func, max_retries=3, retry_delay=5):
    def wrapper(*args, **kwargs):
        for attempt in range(max_retries):
            try:
                return func(*args, **kwargs)
            except (ConnectionError, ConnectionTimeout) as e:
                if attempt < max_retries - 1:
                    logging.warning(f"Connection error: {str(e)}. Retrying in {retry_delay} seconds...")
                    sleep(retry_delay)
                else:
                    logging.error(f"Max retries reached. Failed to execute {func.__name__}")
                    raise
    return wrapper

class VulsElasticIngester:
    def __init__(self, hosts, api_key=None, bulk_size=1000):
        self.es = Elasticsearch(hosts, api_key=api_key)
        self.bulk_size = bulk_size

    def create_index_template(self, template_name, template_body):
        self.es.indices.put_template(name=template_name, body=template_body)

    @retry_on_connection_error
    def ingest(self, normalized_data):
        actions = [
            {
                "_index": f"vuls-scan-{datetime.now().strftime('%Y.%m')}",
                "_source": doc
            }
            for doc in normalized_data
        ]

        success, failed = bulk(self.es, actions, chunk_size=self.bulk_size)
        return success, failed