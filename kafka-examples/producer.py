import json
import random
import uuid
from kafka import KafkaProducer

content = ["I'm happy", "Why do you annoy me?", "That's fine"]

producer = KafkaProducer(bootstrap_servers='localhost:29092')

for _ in range(10):
    msg = json.dumps({'id': uuid.uuid4().hex,
                      'content': random.choice(content)}).encode('utf-8')
    print(msg)
    ack = producer.send('sentiment-ready', msg)
    metadata = ack.get()
