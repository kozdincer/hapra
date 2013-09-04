# -*- coding: utf-8 -*-
from flask import *
from haproxy.haproxy import *
from flask import jsonify

hc = HAProxyConfig('/home/aybuke/repo/hapra/haproxy.cfg')
def makeLink(url):
    return "<a href='%s'>%s</a><br>" %(url, url)

app = Flask(__name__)

@app.route("/")
def index():
    i = ""
    i += makeLink('/get/fnames')
    i += makeLink('/get/lnames')
    i += makeLink('/get/bnames')
    return i

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

if __name__ == "__main__":
    app.debug = True
    app.run(debug= True)

