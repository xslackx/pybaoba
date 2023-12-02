from json import dumps, loads
from collections import Counter

def packFmt(pkgs, id):
    
    if id == "ubuntu":
        packs = pkgs[93:].split("\n")
        
        def fmt(e):
            p = e.split()
        
            return { "name": p[0].split("/")[0],
                    "groups": p[0].split("/")[1].split(','),
                    "version": p[1],
                    "arch": p[2]}
        
        f = list(map(fmt, packs))
        
        return dumps(f)
    
    if id == "fedora":
        packs = pkgs.split()
        for dnflabel in range(2):
            packs.pop(0)
        
        packStorage = []
        packNames = []
        packVersions = []
        packGroups = []

        for x in range(0,len(packs),3):
            packNames.append(packs[x])
            for n in range(1, len(packs), 3):
                packVersions.append(packs[n])
                for i in range(2,len(packs),3):
                    packGroups.append(packs[i])
        
        packs = (list(zip(packNames, packVersions, packGroups)))


        for x in range(len(packs)):
            if x != None:
                packStorage.append(eachPack(packs[x], id))
        #hits = hitCount(dumps(packStorage), id)
        #packStorage.append(hits)

        return dumps(packStorage)


def eachPack(p, i):

    if i == "fedora":

        packName = p[0].split(".")[0]
        packGroup = p[2]
        packVersion = p[1]
        packArch = p[0].split(".")[1]
       
        return {
            "name": packName,
            "groups": packGroup,
            "version": packVersion,
            "arch": packArch
            }

def hitCount(packStorage, id):
    allPacks = loads(packStorage)
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
        if id == "fedora":
            groups.append(allPacks[x]["group"])
        groups.append(allPacks[x]["group"][0])
        
    hit["hits"]["arch"] = Counter(hit64)
    hit["hits"]["group"] = Counter(groups)

    return dumps(hit)