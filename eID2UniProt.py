#!/bin/python

from __future__ import print_function, division
from bs4 import BeautifulSoup
import sys, argparse
try:
    # python > 3.0
    from urllib.request import urlopen
except ImportError:
    # python 2's urllib2
    from urllib2 import urlopen


def get_UniProt_Index(td_list):
	for i in range(len(td_list)):
		#print(td_list[i])
		if "uniprot.org" in str(td_list[i]):
			return td_list[i].text
	return "-"

# Example Input (-i transcriptIDfile ) 
# transcriptID
# ENSMUST00000027186.11
# ENSMUST00000162899.7
# ENSMUST00000219033.1
# ENSMUST00000111303.1
# ENSMUST00000111140.2
# ENSMUST00000154650.7
# ENSMUST00000055676.3
# ENSMUST00000132918.7
# ENSMUST00000077709.10

if __name__ == '__main__':
	
	#USAGE: python eID2UniProt.py -i transcriptIDfile -g mm10 \n')

	reference2Taxon = {"mouse" : "Mus_musculus", "mm10" : "Mus_musculus", "mm9" : "Mus_musculus", "human": "Homo_sapiens", "hg19" : "Homo_sapiens", "hg39" : "Homo_sapiens"}
	
	parser = argparse.ArgumentParser(description='Converts Ensembl transcriptIDs to UniProtKBs')
	parser.add_argument('-i','--input', type=str, required=True, help='Input file of Ensembl TranscriptIDs (newline delimited)')
	parser.add_argument('-g','--referenceGenome', type=str, required=True, help='Mouse or Human')
	parser.add_argument('--header', action='store_true', help='File contains a header')
	args = parser.parse_args()

	iref = args.referenceGenome.lower().strip()
	ref = reference2Taxon[iref]

	# Input Ensembl TranscriptID file 
	fname = args.input
	header_exists = args.header
	
	with open(fname) as fh:
		if header_exists:
			header = next(fh)
		print('transcript_name\ttranscriptID\tbp\tProtein\tUniProt')
		for line in fh:
			linelist = line.strip().split('.')
			transcript = linelist[0].strip()
			#url = 'https://useast.ensembl.org/{}/Gene/Summary?t={}'.format(ref, transcript)
			url = 'http://useast.ensembl.org/{}/Gene/Summary?t={};'.format(ref, transcript)
			page = urlopen(url).read()		
			soup = BeautifulSoup(page, features="html.parser")
			#div = soup.findAll('div', {'class':'transcripts_table'})

			for tr in soup.find_all('tr')[1:]:
				tds = tr.find_all('td')
				print('{}\t{}\t{}\t{}\t{}'.format(tds[0].text, tds[1].text, tds[2].text, tds[3].text, get_UniProt_Index(tds[:])))
