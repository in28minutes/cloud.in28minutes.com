import logging
import os
import random

import google.cloud.pubsub_v1
from flask import Flask

# [logging config
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(filename)s:%(funcName)s:%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)
# logging config]

app = Flask(__name__)
app.secret_key = 'somesecretkey'

topic_path = 'MY_TOPIC_PATH_HERE'
subscription_path = 'MY_SUBSCRIPTION_PATH_HERE'


# http://localhost:5000/send
@app.route('/send', methods=['GET'])
def send():
    """Send"""
    logging.info('Sending message to topic [%s]', topic_path)
    num = random.random()
    data = 'Hello world ' + str(num)
    data = data.encode('utf-8')

    publisher = google.cloud.pubsub_v1.PublisherClient()
    future = publisher.publish(topic_path, data)
    logging.info('Message sent')
    return {
        'status': 'ok',
        'msg': future.result()
    }


# http://localhost:5000/receive
@app.route('/receive', methods=['GET'])
def receive():
    """Receive message from pull subscription"""
    logging.info('Listening messages from subscription [%s]', subscription_path)
    subscriber = google.cloud.pubsub_v1.SubscriberClient()
    pull = subscriber.subscribe(subscription_path, callback)
    with subscriber:  # wrap subscriber 'with' block to automatically call close() when done
        try:
            pull.result(timeout=5)  # block with a timeout
        except TimeoutError:
            pull.cancel()  # trigger the shutdown
            pull.result()  # block until shutdown is complete


def callback(message):
    logging.info('Received message [%s]', message)
    logging.info('Data [%s]', message.data)
    message.ack()


# driver code
if __name__ == '__main__':
    server_port = os.environ.get('PORT', '5000')
    app.run(debug=False, port=server_port, host='0.0.0.0')
