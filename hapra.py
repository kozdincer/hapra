# -*- coding: utf-8 -*-
from flask import *
import os

os.system('touch /home/aybuke/repo/hapra/hapra.wsgi')

app = Flask(__name__)




@app.route("/")
def index():
    i = ""
    i += makeLink('/get/frontendNames')
    return i

def makeLink(url):
    return "<a href='%s'>%s</a><br>" %(url, url)


@app.route("/get/fnames")
def fnames():
























@app.route("/get")
def all():
    return "global, defaults, listen, frontend, backend"
@app.route("/get/global")
def globalh():
    return "global"
@app.route("/get/defaults")
def defaults():
    return "defaults"
@app.route("/get/listen/str:<name>")
def listen(name):
    return "listen name: %s " %name
@app.route("/get/listens")
def listens():
    return "listens"
@app.route("/get/listensName")
def listensName():
    return "listenNames"
@app.route("/get/frontend/str:<name>")
def frontend(name):
    return "frontend name: %s" %name
@app.route("/get/frontends")
def frontens():
    return "frontends"
@app.route("/get/frontendsName")
def frontendsName():
    return "frontendNames"
@app.route("/get/backend/str:<name>")
def backend(name):
    return "backend name: %s" %name
@app.route("/get/backends")
def backends():
    return "backends"
@app.route("/get/backendsName")
def backendsName():
    return "backendNames"

#@app.route("/add/global")
#@app.route("/add/defaults")
#@app.route("/add/listen")
#@app.route("/add/frontend")
#@app.route("/add/backend")


#@app.route("/del/global")
#@app.route("/del/defaults")
#@app.route("/del/listen/<number>")
#@app.route("/del/frontend/<number>")
#@app.route("/del/backend/<number>")


#@app.route("/addOption/global/<param_name>/<params>")
#@app.route("/addOption/defaults/<param_name>/<params>")
#@app.route("/addOption/listen/<number>/<param_name>/<params>")
#@app.route("/addOption/frontend/<number>/<param_name>/<params>")
#@app.route("/addOption/backend/<number>/<param_name>/<params>")


#@app.route("/delOption/global/<param_name>/<params>")
#@app.route("/delOption/defaults/<param_name>/<params>")
#@app.route("/delOption/listen/<number>/<param_name>/<params>")
#@app.route("/delOption/frontend/number/<param_name>/<params>")
#@app.route("/delOption/backend/<number>/<param_name><params>")

if __name__ == "__main__":
    app.run(debug= True)


