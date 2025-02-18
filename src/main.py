import logging
import json
from datetime import datetime
from config import load_config
from normalizer import VulsDataNormalizer
from ingester import VulsElasticIngester

def setup_logging(config):
    logger = logging.getLogger('vuls_ingestor')
    logger.setLevel(config['logging']['level'])

    file_handler = logging.FileHandler(config['logging']['file'])
    file_handler.setLevel(config['logging']['level'])

    class JsonFormatter(logging.Formatter):
        def format(self, record):
            log_record = {
                'timestamp': datetime.utcnow().isoformat(),
                'level': record.levelname,
                'message': record.getMessage(),
                'logger': record.name
            }
            return json.dumps(log_record)

    file_handler.setFormatter(JsonFormatter())
    logger.addHandler(file_handler)
    return logger

def read_vuls_data(path):
    # Implement this function to read Vuls data from the specified path
    # This is a placeholder and should be replaced with actual implementation
    pass

def main():
    config = load_config('config/config.yaml')
    logger = setup_logging(config)

    logger.info("Starting Vuls data ingestion")

    normalizer = VulsDataNormalizer()
    ingester = VulsElasticIngester(
        hosts=config['elasticsearch']['hosts'],
        api_key=config['elasticsearch']['api_key'],
        bulk_size=config['elasticsearch']['bulk_size']
    )

    # Create index template
    ingester.create_index_template('vuls-template', normalizer.index_template)

    # Read Vuls data
    vuls_data = read_vuls_data(config['input']['vuls_results_path'])

    # Normalize data
    normalized_data = normalizer.normalize(vuls_data)

    # Ingest data
    success, failed = ingester.ingest(normalized_data)
    logger.info(f"Ingested {success} documents, {failed} failed")

if __name__ == "__main__":
    main()

{
  "azure_client_secret": "dGhpcyBpcyBhIHRlc3QgY2xpZW50IHNlY3JldCBmb3IgQXp1cmU="
}
# Secret in here my nigga 

{
    "beamer_api_token": "b_qgcef589prlas8cz_o9rk-bhmywcdfjmiqbqy28vg6hb"
}
