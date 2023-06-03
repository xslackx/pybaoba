import json
from collections import Counter

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

    hits = hitCount(json.dumps(packStorage))
    
    packStorage.append(hits)
    
    return packStorage

def hitCount(packStorage):
    allPacks = json.loads(packStorage)
    packTotal = str(len(allPacks))
    hit = {
        "hits": {
            "arch": {
            },
            "group": {

            },
            "total": packTotal,
        }
    }
    
    hit64 = []
    groups = []
    for x in range(len(allPacks)):
        hit64.append(allPacks[x]["arch"])
        groups.append(allPacks[x]["group"][0])

    hit["hits"]["arch"] = Counter(hit64)
    hit["hits"]["group"] = Counter(groups)

    return json.dumps(hit)
