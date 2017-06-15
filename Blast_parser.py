from __future__ import print_function

import re

class BlastReport(object):
    """Store information from one BLAST alignment file.

    Parses the alignment information from one BLAST output file for various data (see `parse_alignments`).
    Regular expressions do the bulk of the matching, along with some of the Python string functions for
    convenience.

    Attributes:
    alignments (list): a list of :class:`Alignment` objects

    """

    Q_NAME_RE = re.compile("Query=\s+(.*?)\s")
    Q_LETTER_RE = re.compile("Length=(\d+)")
    Q_DESC_RE = re.compile("Query=\s+\w+\W+(.+)")
    S_LENGTH_RE = re.compile("^Length\s?=\s?(\d+)$")
    S_NAME_RE = re.compile("^>\s+(gi\|\d+\|gb\|.+?)\|(.+?)\[Es")
    EXPECT_RE = re.compile("Expect\s+=\s+(.+?),")

    def __init__(self, infile):
        """Instantiate a :class:`BlastReport` object.

        Arguments:
        infile (str): the path to the BLAST file to use as an input source.

        """

        self.alignments = []
        self.infile = infile
        self.No_hits = []

    def parse_alignments(self):
        """Parse alignment data for some summary information.

        Step through an alignment data file line by line and pull out
        * Query name
        * Query description
        * Query length ('letters')
        * Subject name
        * Subject description
        * Subject length

        Returns:
        A list of :class:`Alignment` objects containing the summary data.

        """

        query_line = ""
        subj_line = ""
        q_name = q_description = q_length = s_name = s_description = s_length = e_val =  None
        no_hit_flag = query_flag = False



        query_data = None
        for line in self.infile:
            line = line.strip()
            # if we have a current alignment, and encounter a new one, save the current one
            if line.startswith("Query="):
                if e_val:
                    query_data = (q_name, q_description, q_length, s_name, s_description, s_length, e_val)
                    # use the splat operator to unpack the tuple prior to passing it to the
                    # Alignment constructor
                    self.alignments.append(Alignment(*query_data))
                    if e_val == 999:
                        self.No_hits.append((q_name, q_description))
                        print ("Appended")
                    no_hit_flag = query_flag = False

                    #print ("Query reset")
                query_line = line
                name_match = self.Q_NAME_RE.search(line)
                desc_match = self.Q_DESC_RE.search(line)
                if name_match:
                    q_name = name_match.group(1)
                if desc_match:
                    q_description = desc_match.group(1)
            elif query_line and "Length" not in line:
                query_line += " " + line
            elif "Length" in line:

                if (not query_flag) or no_hit_flag :
                    query_line = None
                    len_match = self.Q_LETTER_RE.search(line)
                    if len_match:
                        q_length = len_match.group(1)
                        query_flag = True
                        #no_hit_flag = False
                else:

                    l_match = self.S_LENGTH_RE.search(line)
                    if l_match:
                        s_length = l_match.group(1)
                        #print ("got match")

            elif 'No hits found' in line:

                no_hit_flag = True
                print ("For query", q_name, "there were NO HITS!")
                s_name = s_description = s_length = "NO HIT"
                e_val = 999

            elif line.startswith(">"):
                name_match = self.S_NAME_RE.search(line)
                if name_match:
                    s_name = name_match.group(1)
                    s_description = name_match.group(2)
                    #print ("Got subject name and description")
            elif "Expect" in line:
                #print ("Searching for e-value")
                e_match = self.EXPECT_RE.search(line)
                if e_match:
                    e_val = e_match.group(1)
        query_data = (q_name, q_description, q_length, s_name, s_description, s_length, e_val)
        # make sure to save the last alignment--without this call, it will be cut off
        # use the splat operator to unpack the tuple prior to passing it to the
        # Alignment constructor
        self.alignments.append(Alignment(*query_data))

        return self.alignments

    def write_report(self, alignments, outfile):
        #with open(outfile, 'w') as ofh:
            #for a in alignments:
               # print(a, file=ofh, end='')
        for item in self.No_hits:
            print (item)

        print ("There were", len(self.No_hits), "genes with no hits")


class Alignment(object):
    """Store data about an alignment found in a BLAST report.

    Attributes:
    q_name (str): the name of the query sequence
    q_desc (str): the description of the query sequence
    q_length (int): the length of the query sequence
    s_name (str): the name of the subject sequence
    s_description: not implemented
    s_length (int): the length of the subject sequence
    e_val (float): the expect value of the alignment

    """

    def __init__(self, q_name, q_description, q_length, s_name, s_description, s_length, e_val):
        """Instantiate a :class:`Alignment` object.

        Arguments:
        q_name (str): the name of the query sequence
        q_desc (str): the description of the query sequence
        q_length (int): the length of the query sequence
        s_name (str): the name of the subject sequence
        s_description: not implemented
        s_length (int): the length of the subject sequence
        e_val (float): the expect value of the alignment

        """

        self.q_name = q_name
        self.q_description = q_description
        self.q_length = q_length
        self.s_name = s_name
        self.s_description = s_description
        self.s_length = s_length
        self.e_val = e_val

    def __str__(self):
        return "{} {} {} {} {} {} {}\n".format(self.q_name, self.q_description,
        self.q_length, self.s_name,
        self.s_description, self.s_length, self.e_val)


def main():
    file_name = "results.txt"
    outfile = file_name.replace(".txt", ".out.txt")
    with open(file_name) as infile:
        report = BlastReport(infile)
        alignments = report.parse_alignments()
        report.write_report(alignments, outfile)
        #for thing in alignments:
            #print (thing)







if __name__ == "__main__":
    main()
