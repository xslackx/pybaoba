from .usermsg import loadFile

def packMan(id):
    ids = "conf/supported.json"
    msg = "conf/st_messages.json"

    sys = loadFile(ids)
    msg = loadFile(msg)

    for os in sys["systems"]["ID"]:
        if os == id and id == "fedora" or id == "redhat":
            cmdlet = sys["systems"]["cmd"][0]

        if os == id and id == "debian" or id == "ubuntu":
            cmdlet = sys["systems"]["cmd"][1]

        if os == id and os == "alpine":
            cmdlet = sys["systems"]["cmd"][2]

    if cmdlet == None:
        return msg["status"]["err"]["f05"]

    return cmdlet
