import json

def loadFile(json_file):
    with open(json_file, "r+") as file:
        msg = json.load(file)
        file.close()
    return msg

def userMsg(type, st_code):
    status = "../conf/st_messages.json"
    msg = loadFile(status)
    if type == None or st_code == None:
        return msg["status"]["err"]["f02"]

    if type != 'info' and type != 'ok' and type != 'err':
        return  msg["status"]["err"]["f01"]

    return msg["status"][type][st_code]
