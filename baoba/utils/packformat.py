import json

def packFmt(pkgs, id):
    if id == "ubuntu":
        packs = pkgs.split("\n")
        
        for aptwarning in range(4):
            packs.pop(0)

    def eachPack(p):
        packName = p.split()[0].split("/")[0]
        packGroup = p.split()[0].split("/")[1].split(",")
        packVersion = p.split()[1]
        packArch = p.split()[2] 

        return {
            "name": packName,
            "group": packGroup,
            "version": packVersion,
            "arch": packArch
        }
    
    packStorage = []
    for x in range(len(packs)):
        if x != None:
            packStorage.append(eachPack(packs[x]))

    
    return json.dumps(packStorage)
