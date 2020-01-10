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
	parser.add_argument('--acclinks', required=True, help='(absolute) path to file containing URLs to the accession lists')
	parser.add_argument('--acclists', help='(absolute) path to directory to save the accession lists to')
	args = parser.parse_args()

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
			print('### fetch: ' + filename)
			open(os.path.join(args.acclists,filename),'wb').write(acc.content)
			
			# 
			accDataTable.write(filename + '\t')
			accDataTable.write(os.path.join(args.acclists,filename) + '\n')

		accDataTable.close()
		print('### create tab-separated list '+ accDataTableFile)

		# move list with accession list to /galaxy/tool-data
		shutil.copy(accDataTableFile,os.path.join(args.galaxy,'tool-data/'))
		print('### move tab-separated list to ' + str(os.path.join(args.galaxy,'tool-data/')))
		
# 
if __name__ == "__main__":
	main()
