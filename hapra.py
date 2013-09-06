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
    i += makeLink('/get/listen/appli1-rewrite')
    i += makeLink('/get/frontends')
    i += makeLink('/get/backends')
    i += makeLink('/get/listens')
    return i

@app.route('/get/global')
def globalh():
    g = hc.globalh
    gj = GlobalJSON(g).json
    gj = json.loads(gj)
    return jsonify(status='OK', globalh=gj)

@app.route('/get/defaults')
def defaults():
    d = hc.defaults
    dj = DefaultsJSON(d).json
    dj = json.loads(dj)
    return jsonify(status='OK', defaults=dj)

@app.route('/get/frontend/<name>')
def frontend(name):
    f = hc.getFrontend(name)
    fj = FrontendJSON(f).json
    fj = json.loads(fj)
    return jsonify(status='OK', frontend=fj)

@app.route('/get/backend/<name>')
def backend(name):
    b = hc.getBackend(name)
    bj = BackendJSON(b).json
    bj = json.loads(bj)
    return jsonify(status='OK', backend=bj)

@app.route('/get/listen/<name>')
def listen(name):
    l = hc.getListen(name)
    lj = ListenJSON(l).json
    lj = json.loads(lj)
    return jsonify(status='OK', listen=lj)

@app.route('/get/frontends')
def frontends():
    fs = hc.getFrontends()
    fsa = []
    for f in fs:
        fj = FrontendJSON(f).json
        fj = json.loads(fj)
        fsa.append(fj)
    return jsonify(status='OK', frontends=fsa)

@app.route('/get/backends')
def backends():
    bs = hc.getBackends()
    bsa = []
    for b in bs:
        bj = BackendJSON(b).json
        bj = json.loads(bj)
        bsa.append(bj)
    return jsonify(status='OK', backends=bsa)

@app.route('/get/listens')
def listens():
    ls = hc.getListens()
    lsa = []
    for l in ls:
        lj = ListenJSON(l).json
        lj = json.loads(lj)
        lsa.append(lj)
    return jsonify(status='OK', listens=lsa)

@app.route('/get')
def getall():
    return 'all'

if __name__ == "__main__":
    app.debug = True
    app.run()

