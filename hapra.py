# -*- coding: utf-8 -*-
from flask import *

def makeLink(url):
    return "<a href='%s'>%s</a><br>" %(url, url)

app = Flask(__name__)

@app.route("/")
def index():
    i = ""
    i += makeLink('/get/frontendNames')
    return i

@app.route("/get/fnames")
def fnames():








if __name__ == "__main__":
    app.run(debug= True)




