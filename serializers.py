from haproxy import *
import json

class OptionJSON():
    def __init__(self, oid, option):
        odict = {
            "id" : oid,
            "name" : option.name,
            "params" : option.params
        }
        self.json = json.dumps(odict)

    def getJSON(self):
        return self.json

class GlobalJSON():
    def __init__(self, globalh):
        oa = []
        for index, opt in enumerate(globalh.options):
            oj = OptionJSON(index, opt)
            oa.append(oj.getJSON())
        gdict = {'options' : str(oa)}
        self.json = json.dumps(gdict)
        print self.json

    def getJSON(self):
        return self.json
