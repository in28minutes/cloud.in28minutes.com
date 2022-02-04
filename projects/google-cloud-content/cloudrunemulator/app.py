import os

from flask import Flask

import ctrl
from helper import bootstrap

app = Flask(__name__)


# http://localhost:8080/
@app.route('/', methods=['GET'])
def hello():
    return {'code': 200, 'message': 'hello world!'}


# http://localhost:8080/item/all
@app.route('/item/all', methods=['GET'])
def get_all():
    eles = []
    for todo in ctrl.get_all():
        eles.append({'id': todo[0], 'item': todo[1], 'status': todo[2]})

    return {'code': 200, 'todos': eles, 'count': len(eles)}


# http://localhost:8000/item/1
@app.route('/item/<key>', methods=['GET'])
def get_by_id(key):
    ele = ctrl.get_by_id(key)
    if ele is None:
        return {'code': 404, 'message': 'RESOURCE_NOT_FOUND'}

    return {'code': 200, 'todo': {'id': ele[0], 'item': ele[1], 'status': ele[2]}}


# update and delete - To be implemented...

# main code
if __name__ == '__main__':
    bootstrap()
    server_port = os.environ.get('PORT_NUMBER', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
