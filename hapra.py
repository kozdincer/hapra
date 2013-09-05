# -*- coding: utf-8 -*-
from flask import *
from haproxy.haproxy import *
from flask import jsonify
import json
from serializers import *

hc = HAProxyConfig('/home/aybuke/repo/hapra/haproxy.cfg')

def makeLink(url):
    return "<a href='%s'>%s</a><br>" %(url, url)

app = Flask(__name__)

@app.route("/")
def index():
    i = ""
    i += makeLink('/get/global')
    i += makeLink('/get/defaults')
    i += makeLink('/get/frontend/http_proxy')
    i += makeLink('/get/backend/app')
    return i

@app.route("/get/global")
def globalh():
    g = hc.globalh
    gj = GlobalJSON(g).json
    gj = json.loads(gj)
    return jsonify(status="OK", globalh=gj)

@app.route("/get/defaults")
def defaults():
    d = hc.defaults
    dj = DefaultsJSON(d).json
    dj = json.loads(dj)
    return jsonify(status="OK", defaults=dj)

@app.route("/get/frontend/<name>")
def frontends(name):
    f = hc.getFrontend(name)
    fj = FrontendJSON(f).json
    fj = json.loads(fj)
    return jsonify(status="OK", frontend=fj)

@app.route("/get/backend/<name>")
def backends(name):
    b = hc.getBackend(name)
    bj = BackendJSON(b).json
    bj = json.loads(bj)
    return jsonify(status="OK", backend=bj)

if __name__ == "__main__":
    app.debug = True
    app.run()

