import subprocess
from usermsg import loadFile

def packIns(cmd):
    msg = "../conf/st_messages.json"
    cmdOk = "../conf/supported.json"

    msg = loadFile(msg)
    letcmd = loadFile(cmdOk)

    for permited in letcmd["systems"]["cmd"]:
        if cmd == permited:
            sub = subprocess
            res = sub.getoutput(permited)

    if res:
        return res
