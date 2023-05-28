import json

def loadFile():
    status = "../conf/st_messages.json"
        with open(status, "r+") as file:
            msg = json.load(file)
            file.close()
        return msg

def userMsg(type, st_code):
    msg = loadFile()
    if type == None or st_code == None:
        return msg["status"]["err"]["f02"]

    if type != 'info' and type != 'ok' and type != 'err':
        return  msg["status"]["err"]["f01"]
