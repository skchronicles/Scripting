from __future__ import print_function


def getindexofExtraWSP(mvdlist):
    for pos, mv in enumerate(mvdlist):
        if mv.endswith("\x1d"):
            return pos + 1


def removeExtraWSP(mvdlist):
    mvdstring = mvdlist[-1]
    newstring = mvdstring[:getindexofExtraWSP(mvdstring)]
    mvdlist.pop()
    mvdlist.append(newstring[:-1])
    return mvdlist


if __name__ == "__main__":
    outfile = open("/Users/nbskuhn/Desktop/SQL/reptile_database_2016_12/reptiledb_mvd_long.txt", "w")
    # orgFh = open("reptile_database_2016_08.txt", encoding="mac_centeuro")  # found by encoding_determiner.py
    orgFh = open("/Users/nbskuhn/Desktop/SQL/reptile_database_2016_12/reptiledb_synonym.txt", encoding="UTF-16")
    counter = 0
    for line in orgFh:
        line = line.split("\t")
        #print(line[0])
        pk = line[0]
        mvdlist = line[2:]  # looks at the mvd columns
        #print(mvdlist)
        #print(len(mvdlist))
        mvdlist = mvdlist[:getindexofExtraWSP(mvdlist)]  # removes extra empty indexes
        mvdlist = removeExtraWSP(mvdlist)
        #print(mvdlist)
        for value in mvdlist:
            if len(value) > 3:  # heuristic that seems to work in the odd case something fails
                #outfile.write("{}\t{}\t{}\n".format(pk, line[1], value))  # use this to check to work
                outfile.write("{}\t{}\n".format(pk, value))

        #print("\n")
        #print("#####################################")
    print("---------------done------------------")

    """
    # Checking to see why there is a decrapency between mvd_output and # of db rows in dbfile
    # It has to do with distinct columns
    inFH = open("/Users/nbskuhn/Desktop/SQL/uniq_reptiledb_mvd.txt")
    outFH = open("/Users/nbskuhn/Desktop/SQL/ureptiledb_mvd_withoutQuotes.txt", "w")
    for line in inFH:
        linelist = line.strip(). split("\t")


        if linelist[1].startswith('"') and linelist[1].endswith('"'):
            mvd = linelist[1][1:-1]
            outFH.write("{}\t{}\n".format(linelist[0], mvd))

        elif linelist[1].startswith('"') and not linelist[1].endswith('"'):
            mvd = linelist[1][:-1]
            outFH.write("{}\t{}\n".format(linelist[0], mvd))

        elif not linelist[1].startswith('"') and linelist[1].endswith('"'):
            mvd = linelist[1][1:]
            outFH.write("{}\t{}\n".format(linelist[0], mvd))

        else:
            outFH.write("{}\t{}\n".format(linelist[0], linelist[1]))
    """



