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
    i += makeLink('/all')
    i += makeLink('/global')
    i += makeLink('/defaults')
    i += makeLink('/frontend/http_proxy')
    i += makeLink('/backend/app')
    i += makeLink('/listen/appli1-rewrite')
    i += makeLink('/frontends')
    i += makeLink('/backends')
    i += makeLink('/listens')
    return i

@app.route('/global')
def globalh():
    g = hc.globalh
    gj = GlobalJSON(g).json
    gj = json.loads(gj)
    return jsonify(status='OK', globalh=gj)

@app.route('/defaults')
def defaults():
    d = hc.defaults
    dj = DefaultsJSON(d).json
    dj = json.loads(dj)
    return jsonify(status='OK', defaults=dj)

@app.route('/frontend/<name>')
def frontend(name):
    f = hc.getFrontend(name)
    fj = FrontendJSON(f).json
    fj = json.loads(fj)
    return jsonify(status='OK', frontend=fj)

@app.route('/backend/<name>')
def backend(name):
    b = hc.getBackend(name)
    bj = BackendJSON(b).json
    bj = json.loads(bj)
    return jsonify(status='OK', backend=bj)

@app.route('/listen/<name>')
def listen(name):
    l = hc.getListen(name)
    lj = ListenJSON(l).json
    lj = json.loads(lj)
    return jsonify(status='OK', listen=lj)

@app.route('/frontends')
def frontends():
    fs = hc.getFrontends()
    fsa = []
    for f in fs:
        fj = FrontendJSON(f).json
        fj = json.loads(fj)
        fsa.append(fj)
    return jsonify(status='OK', frontends=fsa)

@app.route('/backends')
def backends():
    bs = hc.getBackends()
    bsa = []
    for b in bs:
        bj = BackendJSON(b).json
        bj = json.loads(bj)
        bsa.append(bj)
    return jsonify(status='OK', backends=bsa)

@app.route('/listens')
def listens():
    ls = hc.getListens()
    lsa = []
    for l in ls:
        lj = ListenJSON(l).json
        lj = json.loads(lj)
        lsa.append(lj)
    return jsonify(status='OK', listens=lsa)

@app.route('/all')
def getall():
    g = hc.globalh
    gj = GlobalJSON(g).json
    gj = json.loads(gj)
    gson = {'global':gj}

    d = hc.defaults
    dj = DefaultsJSON(d).json
    dj = json.loads(dj)
    dson = {'defaults':dj}

    fs = hc.getFrontends()
    fsa = []
    for f in fs:
        fj = FrontendJSON(f).json
        fj = json.loads(fj)
        fsa.append(fj)
    fson = {'frontens':fj}

    bs = hc.getBackends()
    bsa = []
    for b in bs:
        bj = BackendJSON(b).json
        bj = json.loads(bj)
        bsa.append(bj)
    bson = {'backends':bj}

    ls = hc.getListens()
    lsa = []
    for l in ls:
        lj = ListenJSON(l).json
        lj = json.loads(lj)
        lsa.append(lj)
        lson = {'listens':lj}

    config= [gson, dson, fson, bson, lson]
    return jsonify(status='OK', Config=config)

if __name__ == "__main__":
    app.debug = True
    app.run()

