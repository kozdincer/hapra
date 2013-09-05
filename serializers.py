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

