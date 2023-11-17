import os, re
from .usermsg import userMsg, loadFile
from os.path import abspath

def osLike():
    os_release="/etc/os-release"
    os_support="conf/supported.json"
    supported = loadFile(os_support)

    if os.access(os_release, os.R_OK):
        with open(os_release, "r") as f:
            file = f.read()
            file = file.split("\n")
            f.close()

        for key in file:
            if re.match(r"ID=(.*)", key):
                grep = re.match(r"ID=(.*)", key)
                
        if not grep:
            return userMsg('err', 'f04')

        for id in supported["systems"]["ID"]:
            if id == grep[1]:
                return id

        if not id:
            return userMsg('err', 'f03')
    else:
        return userMsg('err', 'f01')
