import pkgutil
import os
import encodings

def all_encodings():
    modnames = set(
        [modname for importer, modname, ispkg in pkgutil.walk_packages(
            path=[os.path.dirname(encodings.__file__)], prefix='')])
    aliases = set(encodings.aliases.aliases.values())
    return modnames.union(aliases)


if __name__ == "__main__":
    filename = 'reptile_database_2016_08.txt'
    encodings = all_encodings()
    for enc in encodings:
        try:
            with open(filename, encoding=enc) as f:
                headerlist = next(f).split("\t")
                # print the encoding and the first 500 characters
                print("Encoding_Type: {}\t\t{} ".format(enc, headerlist))
        except Exception:
            pass