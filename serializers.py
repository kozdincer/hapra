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
            ojs = oj.json
            ojs = json.loads(ojs)
            oa.append(ojs)
        gdict = {'options' : oa}
        self.json = json.dumps(gdict)

    def getJSON(self):
        return self.json

class DefaultsJSON():
    def __init__(self, defaults):
        oa = []
        for index, opt in enumerate(defaults.options):
            oj = OptionJSON(index, opt)
            ojs = oj.json
            ojs = json.loads(ojs)
            oa.append(ojs)
        ddict = {'options': oa}
        self.json = json.dumps(ddict)

class FrontendJSON():
    def __init__(self, frontend):
        oa = []
        for index, opt in enumerate(frontend.options):
            oj = OptionJSON(index, opt)
            ojs = oj.json
            ojs = json.loads(ojs)
            oa.append(ojs)
        fdict = {'options': oa}
        self.json = json.dumps(fdict)


