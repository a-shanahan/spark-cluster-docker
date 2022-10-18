import json
from kafka.errors import NoBrokersAvailable


def send_to_kafka(article, id_, producer):
    """
    Format kafka message and send to topic

    :param article: str
            Text content
    :param id_: str
            Document identifier
    :param producer: Kafka Producer
    :return: None
    """
    try:
        key = list(article.keys())[0]
        msg = json.dumps({'id': id_,
                          'content': article.get(key)['body']}).encode('utf-8')
        ack = producer.send('sentiment-ready', msg)
        _ = ack.get()
    except (AttributeError, NoBrokersAvailable) as e:
        pass
