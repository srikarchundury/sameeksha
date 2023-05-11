import os
import string
import sys

path =  'Tool_Input/' # sys.argv[1]
collections = os.listdir(path)

RunLibrary = dict()

def ParseName(DirName):
	parts = DirName.split('_')
	benchmark = parts[-1]
	type = '_'.join(parts[:-1])
	name = dict()
	name['benchmark'] = benchmark
	name['type'] = type
	return name

def RegisterToLibrary(CollectionInfo):
	benchmark = CollectionInfo['benchmark']
	type = CollectionInfo['type']
	if benchmark not in RunLibrary.keys():
		RunLibrary[benchmark] = []
	if type not in RunLibrary[benchmark]:
		RunLibrary[benchmark].append(type)

def GenerateData():
	for benchmark in RunLibrary.keys():
		print benchmark,RunLibrary[benchmark]
		for type in RunLibrary[benchmark]:
			arg = path+type+'_'+benchmark+'/'
			print arg
			os.system('python format.py '+arg)

for collection in collections:
	CollectionInfo = ParseName(collection)
	RegisterToLibrary(CollectionInfo)
GenerateData()
