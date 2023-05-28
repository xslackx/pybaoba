import usermsg

def packMan(id):
    ids = "../conf/supported.json"
    sys = usermsg.loadFile(ids)

    for os in sys["system"]["ID"]:
        if os == id and os == "fedora" or os == "redhat":
            cmdlet = "dnf list installed"

        if os == id and os == "debian" or os == "ubuntu":
            cmdlet = "apt list --installed"

        if os == id and os == "alpine":
            cmdlet = "apk list -I"

    return cmdlet
