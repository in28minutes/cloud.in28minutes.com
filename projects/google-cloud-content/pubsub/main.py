import logging
import os

import google.api_core.exceptions
import google.cloud.pubsub_v1
import google.pubsub_v1
from flask import Flask, render_template, request, flash, redirect

# [logging config
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(filename)s:%(funcName)s:%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)
# logging config]

app = Flask(__name__)
app.secret_key = 'somesecretkey'


# http://localhost:5000
@app.route('/', methods=['GET'])
def index():
    """Index."""
    logging.info('Showing index page')
    return render_template('form.html')


@app.route('/', methods=['POST'])
def create():
    """Create topic and subscription."""
    project_id = request.form.get('project')
    topic_id = request.form.get('topic')
    subscription_id = request.form.get('subscription')
    logging.info('Creating topic and subscription in project id= [%s]', project_id)

    if project_id == '' or topic_id == '' or subscription_id == '':
        logging.info('Topic or subscription cannot be blank')
        flash('Topic or subscription cannot be empty')
        return redirect(request.url)
    else:
        try:
            logging.info('Creating topic [%s]', topic_id)
            publisher = google.cloud.pubsub_v1.PublisherClient()
            topic_path = publisher.topic_path(project_id, topic_id)
            response = publisher.create_topic(request={'name': topic_path})
            # logging.info(response)
            logging.info('Topic created [%s]', response.name)

            logging.info('Creating subscription [%s]', subscription_id)
            subscriber = google.cloud.pubsub_v1.SubscriberClient()
            subscription_path = subscriber.subscription_path(project_id, subscription_id)
            with subscriber:
                api_request = {
                    'name': subscription_path,
                    'topic': topic_path
                }
                response1 = subscriber.create_subscription(request=api_request)
            # logging.info(response)
            logging.info('Subscription created [%s]', subscription_id)

            flash('Topic and subscription created successfully')
            return redirect('/')
        except google.api_core.exceptions.GoogleAPIError as err:
            logging.error(err)
            flash('Unable to create topic or error. Check application logs')
            return redirect(request.url)


# http://localhost:5000/list
@app.route('/list', methods=['GET'])
def fetch():
    """Index page to list topics or subscriptions."""
    logging.info('Showing index page to list topics or subscriptions')
    return render_template('list.html', data=[])


@app.route('/list', methods=['POST'])
def get():
    """Endpoint to list topics or subscriptions."""
    choice = request.form.get('choice_select')
    project_id = request.form.get('project')
    topic_id = request.form.get('topic')

    if choice == 'topics':
        logging.info('Listing topics in project [%s]', project_id)
        if project_id == '':
            logging.info('Project id is mandatory for listing topics')
            flash('Topic id cannot be empty when choice is topics')
            return redirect(request.url)
        else:
            topics = []
            publisher = google.cloud.pubsub_v1.PublisherClient()
            project_path = 'projects/{pid}'.format(pid=project_id)
            response = publisher.list_topics(request={'project': project_path})
            for topic in response:
                # logging.info(topic)
                topics.append(topic)

            return render_template('list.html', message='Showing topics', data=topics)

    if choice == 'subscriptions':
        logging.info('Listing subscriptions for topic [%s] in project [%s]', topic_id, project_id)
        if project_id == '' or topic_id == '':
            logging.info('Topic or subscription cannot be blank')
            flash('Topic or subscription cannot be empty when choice is subscriptions')
            return redirect(request.url)
        else:
            # todo - to be implemented
            return render_template('list.html', message='', data=[])


if __name__ == '__main__':
    server_port = os.environ.get('PORT', '5000')
    # Development only: run 'python app.py' and open http://localhost:5000
    app.run(debug=False, port=server_port, host='0.0.0.0')
