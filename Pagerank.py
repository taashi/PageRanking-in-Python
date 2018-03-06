import math
import operator
PR={}
newPR={}
d= 0.85
OL={}
IL={}





def populatingInlinks(generatedGraph):
    o = open(generatedGraph, "r")
    listofLinks = o.readlines()
    filteredList = list(map(lambda i: i.strip().split(' '), listofLinks))
    for links in filteredList:
        IL[links[0]] = (links[1:])


populatingInlinks("bfsgraph.txt")


def numberofsources():
    h = 0
    map(lambda f: not IL[f], IL)
    h = h+1
    print("Number of Sources" + " " + str(h))

numberofsources()


def populatingOutlinks():
    list(map(lambda key: OL.update({key:[]}), IL.keys()))
    map(lambda key, value: presentinIL(key, value), IL.items())

    def presentinIL(key, value):
        y = filter(lambda z: IL.__contains__(z), value)
        map(lambda z: OL[z].append(key), y)

populatingOutlinks()



def computingPageRank():
    NumberofOutlinks = {}
    for k in IL.keys():
        ILcatalog = IL[k]
        w = filter(lambda entry: NumberofOutlinks.__contains__(entry), ILcatalog)
        for entry in w:
            NumberofOutlinks[entry] = NumberofOutlinks[entry] + 1
        n = filter(lambda entry: not NumberofOutlinks.__contains__(entry), ILcatalog)
        for entry in n:
            NumberofOutlinks[entry] = 1
    sinkPages = (list(set(IL.keys()) - set(NumberofOutlinks.keys())))
    print("Number of sinks", len(sinkPages))
    numberofPages = len(IL.keys())
    inc = 0
    iter = 0
    perplexity = 0
    for p in IL.keys():
        PR[p] = (1.0/numberofPages)
    while inc < 4:
        sinkPR = 0
        iter +=1
        print("Perplexity" + " " + str(iter) +" " +str(perplexity))
        oldPerplexity = perplexity
        for p in sinkPages:
            sinkPR = sinkPR + PR[p]
        for p in IL.keys():
            newPR[p] = (1-d)/numberofPages
            newPR[p] += d * sinkPR/numberofPages
            for q in IL[p]:
                newPR[p] += d * PR[q]/(NumberofOutlinks[q])
        for p in IL.keys():
            PR[p] = newPR[p]

        hPR = 0
        for i in IL.keys():
            v = math.log(float(PR[i]), 2)
            hPR = hPR + PR[i] * v
        perplexity = math.pow(2, -hPR)
        if abs(oldPerplexity - perplexity) < 1:
            inc = inc + 1
        else:
            inc = 0

computingPageRank()

def arrangefinalscoreInlinks():
    countInlink = {}
    for s in IL:
        if s in IL:
            data = IL[s]
        countInlink[s] = len(data)
    rankInlink = sorted(countInlink.items(), key=operator.itemgetter(1), reverse=True)
    q = open("IL.txt", "w")
    for rank in range(50):
        q.write(str(rankInlink[rank]) + "\n")


def arrangefinalscorePR():
    rankPR = sorted(PR.items(), key=operator.itemgetter(1), reverse=True)
    e = open("PRG1.txt", "w")
    for m in rankPR[0:50]:
        e.write(str(m)+"\n")



arrangefinalscoreInlinks()




arrangefinalscorePR()






