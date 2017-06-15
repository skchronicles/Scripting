test = str

if test == str:
    print("Yes")
sequene = "TGCTAGCTCGCTCTGCTAGCTCGCTCTGCTAGCTCGCTC"


def revComp(sequence):
    compdict = {"A": "T", "G": "C", "T": "A", "C": "G"}
    revseq = sequence[::-1]
    revcomp = ""
    for base in revseq:
        revcomp += compdict[base]
    return revcomp

recom = revComp(sequene)
print(recom)

codontable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }

seq1 = "ATGAAATTTTAG"
#       01234567
aa = ""
for pos in range(0,len(seq1)-2,3):
    codon = seq1[pos:pos+3]
    print(codon)
    aa += codontable[codon]
    print(aa)

dict = {'>seq2': 'HRQ*TQAV', '>seq3': 'C*LALLARSASSL', '>seq1': 'TAASYCCELLLRATAASYCCE'}

for header in sorted(dict.keys()):
    print(header)

##############################
print("\nLooping Through a File")
testFh = open("fasta.fa", "r")
indexCounter = {}

# Nested Dictionaries: Dat Big-O doe...
for line in testFh:
    line = line.strip()
    if not line.startswith(">"):
        for pos, base in enumerate(line):
            if pos not in indexCounter:  # create the first key
                indexCounter[pos] = {}
            if base not in indexCounter[pos]:  # create the second key
                indexCounter[pos][base] = 1
            else:
                indexCounter[pos][base] += 1
print(indexCounter)

