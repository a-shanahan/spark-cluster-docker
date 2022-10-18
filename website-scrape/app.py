import logging
import time
import uuid
from kafka import KafkaProducer
from scrape import WebSite
from utils import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Kafka connection details. URL name is docker name
producer = KafkaProducer(bootstrap_servers='localhost:29092', api_version=(0, 10, 1))


def main(link):
    """
    Main function to scrape content and call Kafka producer
    :param link: str
                Website link
    :return: None
    """
    step = 1
    while True:
        logger.info(f'Loop: {step}')
        content = WebSite(link).news
        for article in content:
            article_id = uuid.uuid4().hex
            send_to_kafka(article, article_id, producer)
        time.sleep(60)
        step += 1
        if step > 10:
            break


if __name__ == '__main__':
    url = 'https://www.bbc.com/news'
    index = 'bbc-news'
    main(url)
