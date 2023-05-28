import usermsg

def packMan(id):
    ids = "../conf/supported.json"
    sys = usermsg.loadFile(ids)

    for os in sys["systems"]["ID"]:
        if os == id and id == "fedora" or id == "redhat":
            cmdlet = "dnf list installed"

        if os == id and id == "debian" or id == "ubuntu":
            cmdlet = "apt list --installed"

        if os == id and os == "alpine":
            cmdlet = "apk list -I"

    return cmdlet
