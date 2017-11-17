""" hello.py """

import logging
import socket

from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
from flask import Flask, jsonify

log = logging.getLogger(__name__)
app = Flask(__name__)

xray_recorder.configure(service='Front')
XRayMiddleware(app, xray_recorder)
plugins = ('ECSPlugin')
xray_recorder.configure(plugins=plugins)
patch_all()

@app.route('/')
def hello():
    return jsonify({
        'hello': 'world',
        'host': socket.gethostname()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0')
