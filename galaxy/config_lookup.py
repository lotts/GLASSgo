#!/usr/local/bin/python3

'''
This script downloads lookup tables and integrates these into the Galaxy instance

USAGE 
		config_lookup.py --galaxy GALAXY --acclinks ACCLINKS [--acclists ACCLISTS]

OPTIONS 
		-h, --help           show this help message and exit

'''

import os
import argparse
import requests
import sys
import shutil

def main():
	# parse arguments
	parser = argparse.ArgumentParser(description='incorporate the accession lists in GLASSgo/Galaxy to enable clade-specific searches')
	parser.add_argument('--galaxy', required=True, help='(absolute) path to the root directory of the Galaxy instance')
	parser.add_argument('--acclinks', help='(absolute) path to file containing URLs to the accession lists')
	parser.add_argument('--acclists', help='(absolute) path to directory to save the accession lists to')
	args = parser.parse_args()

	# load taxonomic rank and 
	rank = {}
	rank["Alphaproteobacteria"] = {"tax": 28211, "rank": "class"}
	rank["Aquificae"] = {"tax": 200783, "rank": "phylum"}
	rank["Archaea"] = {"tax": 2157, "rank": "superkingdom"}
	rank["Armatimonadetes"] = {"tax": 67819, "rank": "phylum"}
	rank["Bacteria"] = {"tax": 2, "rank": "superkingdom"}
	rank["Bacteroidetes"] = {"tax": 976, "rank": "phylum"}
	rank["Caldiserica"] = {"tax": 67814, "rank": "phylum"}
	rank["Chlamydiae"] = {"tax": 204428, "rank": "phylum"}
	rank["Chloroflexi"] = {"tax": 200795, "rank": "phylum"}
	rank["Chrysiogenetes"] = {"tax": 200938, "rank": "phylum"}
	rank["Cyanobacteria"] = {"tax": 1117, "rank":"phylum"}
	rank["Deferribacteres"] = {"tax": 200930, "rank": "phylum"}
	rank["Deinococcus-thermus"] = {"tax": 1297, "rank": "phylum"}
	rank["Dictyoglomi"] = {"tax": 68297, "rank": "phylum"}
	rank["Elusimicrobia"] = {"tax": 74152, "rank": "phylum"}
	rank["Fibrobacteres"] = {"tax": 65842, "rank": "phylum"}
	rank["Firmicutes"] = {"tax": 1239, "rank": "phylum"}
	rank["Fusobacteria"] = {"tax": 32066, "rank": "phylum"}
	rank["Gemmatimonadetes"] = {"tax": 142182, "rank": "phylum"}
	rank["Nitrospinae"] = {"tax": 1293497, "rank": "phylum"}
	rank["Nitrospirae"] = {"tax": 40117, "rank": "phylum"}
	rank["Planctomycetes"] = {"tax": 203682, "rank": "phylum"}
	rank["Proteobacteria"] = {"tax": 1224, "rank": "phylum"}
	rank["Spirochaetes"] = {"tax": 203691, "rank": "phylum"}
	rank["Synergistetes"] = {"tax": 508458, "rank": "phylum"}
	rank["Tenericutes"] = {"tax": 544448, "rank": "phylum"}
	rank["Thermodesulfobacteria"] = {"tax": 200940, "rank": "phylum"}
	rank["Thermotogae"] = {"tax": 200918, "rank": "phylum"}
	rank["Viruses"] = {"tax": 10239, "rank": "phylum"}


	# ./accession_lists_links.txt as default
	if args.acclinks == None:
		args.acclinks = os.path.join(os.getcwd(), 'accession_lists_links.txt')

	# ./acclists as default folder for the accession lists
	if args.acclists == None:
		args.acclists = os.path.join(os.getcwd(),'acclists')

	# check for existence of the folders for galaxy and URLs to the accession lists
	if not os.path.exists(args.galaxy):
		print('\tERROR: ' + args.galaxy + ' could not be found!')
		sys.exit()	
	if not os.path.exists(args.acclinks):
		print('\tERROR: ' + args.acclinks + ' could not be found!')
		sys.exit()

	print('################ configure the accession lists ################')
	print('### the accession lists will be saved to ' + args.acclists)

	# create folder for accession lists
	if not os.path.exists(args.acclists):
		os.makedirs(args.acclists)

	# 
	with open(args.acclinks, 'r') as link:
		# create list with lookup tables that populates the user interface
		accDataTableFile = os.path.join(os.getcwd(),'tool-data/glassgo_accession_list.txt')
		
		accDataTable = open(accDataTableFile,'w')
		accDataTable.write('global\tglobal\n')
		# fetch accession lists 
		for url in link:
			acc = requests.get(url)
			filename = str(os.path.basename(url)).replace('\n','')
			filenameStem = str(os.path.splitext(filename)[0])

			#filename = str(os.path.basename(url)).replace('\n','')
			print('### fetch: ' + filename)
			open(os.path.join(args.acclists,filename),'wb').write(acc.content)
			
			# 
			if filenameStem in rank:
				taxid = str(rank[filenameStem]["tax"])
				rankname = rank[filenameStem]["rank"]
				filenameStem = filenameStem + ' (tax:' + taxid + ', rank:' + rankname + ')'
				
			accDataTable.write(filenameStem + '\t')	
			accDataTable.write(os.path.join(args.acclists,filename) + '\n')

		accDataTable.close()
		print('### create tab-separated list '+ accDataTableFile)

		# move list with accession list to /galaxy/tool-data
		shutil.copy(accDataTableFile,os.path.join(args.galaxy,'tool-data/'))
		print('### move tab-separated list to ' + str(os.path.join(args.galaxy,'tool-data/')))
		
# 
if __name__ == "__main__":
	main()
