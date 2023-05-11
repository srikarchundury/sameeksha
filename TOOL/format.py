import os
import string
import sys

path =  sys.argv[1]
files = os.listdir(path)

def real_value(x):
	convert = {}
	convert["million"]=1000000
	convert["billion"]=1000000000
	x = string.split(x,'.')[0]
	x = string.split(x,'_')[1:]
	num = int(x[0])
	if(len(x)==2):
		num *= convert[x[1]]
	return num

# files.sort(key=real_value)

parameters = []
data = []
headers = []

f = open(path+files[0])
for line in f:
	parameters.append(line.split('\t')[1])
	data.append(line.split('\t')[1])
# print len(data)

def push(list):
	for i in range(0,len(data)):
		# print i
		data[i] += '\t'+list[i]

for file in files:
	# print file
	f = open(path+file,'r')
	temp = []
	for line in f:
		temp.append(line.split('\t')[2][:-2])
	# print temp
	push(temp)
	f.close()

for i in files:
	temp = string.split(i,'.')[0]
	headers.append(temp[:4])

data[0] = '\t'.join(headers)
data = data[:83]
output = string.split(path,'/')[-2]
OutputPath = 'Tool_Data/'
os.system('mkdir -p '+OutputPath)
o = open(OutputPath+output+".csv",'w')
for line in data:
	o.write(str(line))
	o.write('\n')
o.close()
