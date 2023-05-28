import usermsg

def packMan(id):
    ids = "../conf/supported.json"
    msg = "../conf/st_messages.json"

    sys = usermsg.loadFile(ids)
    msg = usermsg.loadFile(msg)

    for os in sys["systems"]["ID"]:
        if os == id and id == "fedora" or id == "redhat":
            cmdlet = "dnf list installed"

        if os == id and id == "debian" or id == "ubuntu":
            cmdlet = "apt list --installed"

        if os == id and os == "alpine":
            cmdlet = "apk list -I"

    if cmdlet == None:
        return msg["status"]["err"]["f05"]

    return cmdlet
