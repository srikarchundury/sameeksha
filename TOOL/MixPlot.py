import os
import img2pdf
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys
import string

path = "C:\\Users\\srama\\Documents\\GitHub\\Sameeksha\\TOOL\\Tool_Data\\"
files = os.listdir(path)
PlotData = dict()

count = 0
Clusters = 0

for file in files:
	name= file.split('.')[0]
	file = path+file
	file = open(file)
	data = []
	headers = []
	for i in file:
		s=i[:-1]
		data.append(s.split('\t'))
		# print(s.split('\t'))
	file.close()
	headers = data[0]
	Clusters = len(headers)
	data = data[1:-1]
	count = len(data)
	PlotData[name] = dict()
	PlotData[name]['h'] = headers
	PlotData[name]['d'] = data


names = PlotData.keys()
ClusterSize = len(names)
headers = []
data = []
colors=['green', 'blue', 'cyan', 'orange', 'black', 'red']
with PdfPages('./Tool_Output/'+"Output"+'.pdf') as pdf:
	for c in range(0,count):
		size = ClusterSize * Clusters
		colors = colors[:ClusterSize]
		data = list('0'*size)
		headers = list('0'*size)
		title = ""
		for name in names:
			d = PlotData[name]['d'][c][1:]
			h = PlotData[name]['h']
			title = PlotData[name]['d'][c][0]
			pos = list(names).index(name)
			for i in d:
				# print(pos)
				data[pos] = i
				pos += ClusterSize
			pos = list(names).index(name)
			for i in h:
				headers[pos] = i
				pos += ClusterSize
		n = len(headers)
		y = [i for i in range(0,n)]
		y = []
		for i in range(0,Clusters):
			i*=ClusterSize+1
			j=0
			while(j<ClusterSize):
				y.append(i+j)
				# y.append(i)
				j+=1

		print(title)
		for num in range(0,n):
			data[num] = eval(data[num])

		plt.clf()
		plt.bar(y, data, align='center', alpha=0.5, color=colors, edgecolor='black', width=1.0)
		plt.xticks(y, headers,rotation=90)
		plt.ylabel(title)
		plt.title(name)
		names = list(names)
		leg = list('0'*ClusterSize)
		for i in range(0,len(leg)):
			leg[i] = mpatches.Patch(color=colors[i], label=names[i])
		plt.legend(handles=leg, loc=2)
		plt.tight_layout()
		pdf.savefig()
		# plt.show()
