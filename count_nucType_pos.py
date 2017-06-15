fH = open("testfasta.txt", "r")


def findmaxcount(countdict):
    maxcount = -999
    returnNuc = ""
    tie = ""
    for nuc, count in countdict.items():
        if count > maxcount:
            maxcount = count
            returnNuc = nuc
        elif count == maxcount:
            tie = nuc
    if tie:
        return "("+returnNuc+"*"+")"
    else:
        return returnNuc

indexcountsdict = {}
for line in fH:
    line = line.strip()
    if not line.startswith(">"):
        #print(line)
        for pos, nuc in enumerate(line):
            if pos not in indexcountsdict:
                indexcountsdict[pos] = {}
                if nuc not in indexcountsdict[pos]:
                    indexcountsdict[pos][nuc] = 1
            else:
                if nuc not in indexcountsdict[pos]:
                    indexcountsdict[pos][nuc] = 1
                else:
                    indexcountsdict[pos][nuc] += 1
print(indexcountsdict)
fH.close()

conseq = ""
for index, nucdict in indexcountsdict.items():
    print(index, nucdict)
    conseq += findmaxcount(nucdict)
print(conseq)  # if there is a tie for the second highest count a star will appear after the printed char



