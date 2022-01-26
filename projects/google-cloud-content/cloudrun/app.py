import os
from datetime import datetime

from flask import Flask

app = Flask(__name__)


# http://localhost:8080/
@app.route('/', methods=['GET'])
def hello_world():
    """Return a friendly greeting."""
    return {'code': '200', 'message': 'Welcome to the in28minutes tutorials!'}


# http://localhost:8080/timestamp
@app.route('/timestamp', methods=['GET'])
def get_timestamp():
    """Return current timestamp."""
    now = datetime.now()
    timestamp = now.strftime('%d-%m-%y') + "-" + now.strftime("%H:%M:%S")
    return {'code': '200', 'time_stamp': timestamp}


# driver code
if __name__ == '__main__':
    # Development only: run "python app.py" and open http://localhost:8080
    # In production WSGI HTTP server, such as Gunicorn, will serve the app.
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
