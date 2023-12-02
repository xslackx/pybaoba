import subprocess
from .usermsg import loadFile

def packIns(cmd, ssh: bool):
    msg = "conf/st_messages.json"
    cmdOk = "conf/supported.json"

    msg = loadFile(msg)
    letcmd = loadFile(cmdOk)

    for permited in letcmd["systems"]["cmd"]:
        if cmd == permited:
            if not ssh:
                sub = subprocess
                res = sub.getoutput(permited)
            else:
                return permited

    if res:
        return res
