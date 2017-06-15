# Used for Database Normalization: Creates Multivalued Relations (4NF) from un-normalized data.
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



