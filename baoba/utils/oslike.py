import os, usermsg

def osLike():
    os_release="/etc/os-release"
    if os.access(os_release, os.R_OK):
        with open(os_release, "r") as f:
            file = f.read()
            f.close()
        return file.split("\n")
    else:
        msg = usermsg.userMsg('err', 'f01')
        return msg
