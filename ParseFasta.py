#####################################################
# Skyler Kuhn and Hasan Alkhairo
# BNFO420: FASTA-format Parser
#####################################################
from __future__ import print_function
from __future__ import division


class ParseFasta:
    def __init__(self, fastafile):
        self.fastafile = fastafile
        self.header = ""
        self.sequence = ""
        self.sequencecount = 0
        self.basepaircount = 0
        self.fastaDict = {}
        self.BaseFreqDict = {}

    def parse(self):
        with open(self.fastafile) as fasta:
            for line in fasta:
                #print(line)
                line = line.strip()
                #if line[0] == ">":
                #if ">" in line:
                if line.startswith(">"):
                    self.sequencecount += 1
                    if self.sequence != "":
                        self.fastaDict[self.header] = self.sequence
                        self.sequence = ""
                    self.header = line   # >seq1, >seq2, >seq3
                else:
                    self.sequence += line
            else:  # we need to grab the last sequence and its annotation
                self.fastaDict[self.header] = self.sequence

            return self.fastaDict

    @staticmethod
    def revComp(sequence):
        compdict = {"A":"T", "G":"C", "T":"A", "C":"G"}
        revseq = sequence[::-1]
        revcomp = ""
        for base in revseq:
            revcomp += compdict[base]
        return revcomp

    @staticmethod
    def translate(sequence):
        codontable = {
            'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
            'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
            'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
            'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
            'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
            'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
            'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
            'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
            'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
            'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
            'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
            'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
            'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
            'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
            'TAC': 'Y', 'TAT': 'Y', 'TAA': '*', 'TAG': '*',
            'TGC': 'C', 'TGT': 'C', 'TGA': '*', 'TGG': 'W'}
        aminoacid = ""
        for pos in range(0,len(sequence)-2,3):
            codon = sequence[pos:pos+3]
            aminoacid += codontable[codon]
        return aminoacid

    def seqcount(self):
        return self.sequencecount

    def findnuccontents(self):
        fastaDict = self.parse()
        for sequence in fastaDict.values():
            for base in sequence:
                self.basepaircount += 1
                if base not in self.BaseFreqDict:
                    self.BaseFreqDict[base] = 1
                else:
                    self.BaseFreqDict[base] += 1

        for base, count in self.BaseFreqDict.items():
            self.BaseFreqDict[base] = count/float(self.basepaircount)
        return self.BaseFreqDict

class TransformFasta:
    def __init__(self, fastafile, fastadictionary=None):
        self.fastafile = fastafile
        self.fastadictionary= fastadictionary
        self.AAdictionary = {}

        if self.fastafile:  # using the parsefasta class to create a dictioanry fastafile container
            self.fastadictionary = ParseFasta(fastafile=self.fastafile).parse()

    def translate(self):
        codontable = {
            'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
            'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
            'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
            'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
            'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
            'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
            'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
            'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
            'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
            'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
            'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
            'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
            'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
            'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
            'TAC': 'Y', 'TAT': 'Y', 'TAA': '*', 'TAG': '*',
            'TGC': 'C', 'TGT': 'C', 'TGA': '*', 'TGG': 'W'}
        for header, seq in self.fastadictionary.items():
            aa = ""
            for pos in range(0,len(seq)-2,3):
                codon = seq[pos:pos+3]
                aa += codontable[codon]
            self.AAdictionary[header] = aa
        return self.AAdictionary

    def writefasta(self, dict):
        fH = open("new_fasta.fa","w")
        for header in sorted(dict.keys()):
            fH.write("{}\n{}\n".format(header, dict[header]))
        print("Writing to new file...")
        fH.close()


def main():

    # ------- Validating the Fasta Parsing Object --------- #
    print("\n---- Fasta File Dictionary ---------------> ")
    fastaDict = ParseFasta(fastafile="fasta.fa").parse()
    print("{}\n".format(fastaDict))


    # ------- Finding Nucleotide Content of all the Sequences --------- #
    print("---- Nucleotide Content -------------------> ")
    BaseFreqs = ParseFasta(fastafile="fasta.fa").findnuccontents()
    print("{}\n".format(BaseFreqs))

    # ------- Finding Reverse Complements of all the Sequences --------- #
    print("---- Reverse Complements ------------------> ")
    for header,seq in fastaDict.items():
        #revcomp = ParseFasta.revComp(seq)
        aa = ParseFasta.translate(seq)
        print(header, aa)
        # print(header,revcomp)
    print()

    # ---- Unit Testing ----- #
    seq1 = "ATGAAACCCTTTTGA"
    print("---- Unit Testing -------------------------> ")
    rev_seq1 = ParseFasta.revComp(seq1)
    aa = ParseFasta.translate("ATGAAACCCTTTTGA")
    rev_aa = ParseFasta.translate(rev_seq1)
    print("Sequence:\t\t\t\t\t{}".format(seq1))
    print("Translated Amino Acid:\t\t{}".format(aa))
    print("Translated Reverse Comp:\t{}".format(rev_aa))

    # ---- Testing TransformFasta ----- #
    print("\n---- Testing TransformFasta ----------------> ")
    aaDict = TransformFasta("fasta.fa").translate()
    TransformFasta("fasta.fa").writefasta(aaDict)
    print(aaDict)



if __name__ == "__main__":
    main()


