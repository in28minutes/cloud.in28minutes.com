import datetime
import os

from flask import Flask, render_template
from google.cloud import datastore

# os.environ['DATASTORE_EMULATOR_HOST'] = 'localhost:8484'
# os.environ['DATASTORE_PROJECT_ID'] = 'testproject'

app = Flask(__name__)

client = datastore.Client()


def store_time(now):
    # add object to db
    entity = datastore.Entity(key=client.key('visit'))
    entity.update({
        'timestamp': now
    })

    client.put(entity)


def fetch_times(limit):
    # query from db
    query = client.query(kind='visit')

    return query.fetch(limit=limit)


# http://localhost:8080/
@app.route('/', methods=['GET'])
def index():
    timestamp = datetime.datetime.now(tz=datetime.timezone.utc)

    store_time(now=timestamp)

    times = fetch_times(limit=10)

    return render_template('index.html', times=times)


if __name__ == '__main__':
    server_port = os.environ.get('PORT_NUMBER', '8080')

    app.run(debug=False, port=server_port, host='0.0.0.0')
