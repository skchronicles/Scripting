###############################################################################
# Skyler Kuhn
# BNFO 601: Integrative Bioinformatics
# Exam Question_1: Convert GenPept formatted file into a FASTA formatted File
###############################################################################

from __future__ import print_function
import textwrap
import re


class GenPeptParser(object):
    """
    This class will parse through the GenPept Formatted file and will grab pertinent data to create a FASTA file.
    Regular expressions are employed to do the bulk of pattern matching.

    Attributes:
    matches (list): a list of :class:`Match` objects
    """
    # Regular Expressions: comments show what is grabbed (Everything in Parenthesis is grabbed)
    GI_GB_NUMBERS_RE = re.compile("^VERSION\s+(\w+.\w+)\s+\w+:?(\d+)")   # VERSION     (EGR65295.1)  GI:(340736247)
    DEFINITION_RE = re.compile("^DEFINITION\s+([^\[\,]+)")               # DEFINITION (3-isopropylmalate) [Escheric...\n
    ORGANSIM_RE = re.compile("^SOURCE\s+(.*)")                           # SOURCE  (Escherichia coli O104:H4 str. 01-591)
    # ^I am doing this because the definition gets cut off onto a new line sometimes
    SEQUENCE_RE = re.compile("^\d{1,4}\s+(\w+.*)")                       # 1 (msknyhiavl pgdgigpevm tqalkvldav rnr...\n)
    # ^Will have to used the replace function to remove the spaces in between the AA sequences

    def __init__(self, infile):
        """Instantiate a :class:`GenPeptParser` object.
        Arguments:
        infile (str): the path to the BLAST file to use as an input source.
        """
        self.matchlist = []
        self.infile = infile
        self.prot_sequence = ""

    def parse_file(self):
        """Parse GenPept data for some summary information.

                Step through an GenPept file line by line and pull out
                * GI Number
                * GB/something else Number
                * Definition
                * Sequence

                Returns:
                A list of :class:`Matches ` objects containing the pertinent data.
        """

        gb_number = gi_number = annonation_dec = organism = nospace_seq = None

        for line in self.infile:
            line = line.strip()
            if line.startswith("LOCUS"):
                if gb_number and gi_number and annonation_dec and organism and nospace_seq:
                    data = (gb_number, gi_number, annonation_dec, organism, nospace_seq)
                    # use the splat operator to unpack the tuple prior to passing it to the Matches constructor
                    self.matchlist.append(Matches(*data))
                    self.prot_sequence = ""
            gi_gb_match = self.GI_GB_NUMBERS_RE.search(line)
            definition_match = self.DEFINITION_RE.search(line)
            organism_match = self.ORGANSIM_RE.search(line)
            sequence_match = self.SEQUENCE_RE.search(line)
            if gi_gb_match:
                gb_number = gi_gb_match.group(1)
                gi_number = gi_gb_match.group(2)
            if definition_match:
                annonation_dec = definition_match.group(1)
            if organism_match:
                organism = organism_match.group(1)
            if sequence_match:
                self.prot_sequence += sequence_match.group(1)
                nospace_seq = self.prot_sequence.replace(" ", "").upper()  # this is to remove spaces
        data = (gb_number, gi_number, annonation_dec, organism, nospace_seq)
        self.matchlist.append(Matches(*data))
        return self.matchlist


    def write_report(self, matches, outfile):
        with open(outfile, 'w') as ofh:
            for match in matches:
                print(match, file=ofh, end='')

class Matches(object):
    """Stores Information related to the matches, structures it for FASTA format"""

    def __init__(self, gb_number, gi_number, annonation_dec, organism, nospace_seq):
        """Instantiate a :class:`Alignment` object.

        Arguments:
        gb_number (int): the gb number of a seqeunce
        gi_number (int): the gi number of a sequence
        annonation_dec (str): the annotated description of the sequence
        organism (str): the origin of the sequence
        nospace_seq (str): the sequence corresponding to this GenPept file.
        """

        self.gb_number = gb_number
        self.gi_number = gi_number
        self.annonation_dec = annonation_dec
        self.organism = organism
        self.nospace_seq = nospace_seq
        self.length = len(self.nospace_seq)

    """
    def __format__(self, seqformat):
        if seqformat == 'fastaseq':
            for i in range(0, self.length + 1, 64):
                j = i + 64
                print(seqformat[i:j])
    """

    def __str__(self):
        return ">gi|{}|gb|{}| {}\n[{}]\n{}\n{} \n".format(self.gi_number, self.gb_number, self.annonation_dec,
                                          self.organism, textwrap.fill(self.nospace_seq, 64), self.length)


def main():
    file_name = "O104_H4_GP.txt"
    outfile = file_name.replace("GP.txt", "FASTA.txt")
    with open(file_name) as infile:
        fasta = GenPeptParser(infile)
        conversions = fasta.parse_file()
        fasta.write_report(conversions, outfile)

        for thing in conversions:
            print (thing)


if __name__ == "__main__":
    main()