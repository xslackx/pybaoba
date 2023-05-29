import subprocess, json, usermsg

def packIns(cmd):
    msg = "../conf/st_messages.json"
    cmdOk = "../conf/supported.json"

    msg = usermsg.loadFile(msg)
    letcmd = usermsg.loadFile(cmdOk)

    for permited in letcmd["systems"]["cmd"]:
        if cmd == permited:
            sub = subprocess
            res = sub.getoutput(permited)

    if res:
        return res
