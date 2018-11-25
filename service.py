import os
import json
import requests

from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources='*')

@app.route('/')
def hello_world():
    branch = dict()
    if not os.environ['UPSTREAM_SERVICE']:
        chain = []
    else:
        url = "http://" + os.environ['UPSTREAM_SERVICE'] + "." + os.environ['BRANCH'] + "-" + os.environ['UPSTREAM_SERVICE'] + ":" + os.environ['UPSTREAM_PORT']
        request = requests.get(url, timeout=0.5)
        chain = json.loads(request.text)

    branch[os.environ['THIS_SERVICE']] = os.environ['BRANCH']
    chain.append(branch)
    return json.dumps(chain)

@app.route('/me')
def me():
    return "I am service: <b>" + os.environ['THIS_SERVICE'] + "</b> from branch: <b>" + os.environ['BRANCH'] + "</b>"

@app.route('/healthz')
def healthz():
    return "OK"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8080')

