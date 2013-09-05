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

@app.route("/get/fnames")
def fnames():
    fnames = hc.getFnames()
    fdict = {'fnames' : fnames}
    return jsonify(fdict)

@app.route("/get/lnames")
def lnames():
    lnames = hc.getLnames()
    ldict = {'lnames': lnames}
    return jsonify(ldict)

@app.route("/get/bnames")
def bnames():
    bnames = hc.getBnames()
    bdict = {'bnames': bnames}
    return jsonify(bdict)

@app.route("/get/frontend/<name>")
def getFrontend(name):
    return name

@app.route("/get/option")
def getOption():
    o = Option("a", ("dsa", "dsa",))
    oj = OptionJSON(1, o)
    return oj.getJSON()


if __name__ == "__main__":
    app.debug = True
    app.run()

