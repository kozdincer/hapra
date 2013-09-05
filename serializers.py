#!/usr/bin/python
from haproxy import *
from flask import jsonify

class OptionJSON():
    def __init__(self, ):
        pass

    def d(self):
        odict = {'id': id, 'param_name': name, 'params': params}
        return jsonify(odict)

