import os
import pickle
import img2pdf
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys
import string

file = open('input_sizes','r')
size = []
for line in file:
	size.append(int(line[:-1]))

with open('TOOL/data.pickle', 'rb') as handle:
    data = pickle.load(handle)


benchmarks = list(data.keys())
parameters = []
# print(data[benchmarks[0]]['h'])
for i in data[benchmarks[0]]['d']:
	parameters.append(i[0])


with PdfPages('Analysis'+'.pdf') as pdf:
	for p in parameters:
		comp = []

		for b in benchmarks:
			for i in data[b]['d']:
				if i[0] == p:
					print(p)
					comp.append(i[1:])

		# print(comp)

		y=[]
		for i in range(0,len(data[benchmarks[0]]['h'])):
			y.append(i+1)

		y = [1,10,20,30,40,50]

		# plt.plot(size)
		count = 0
		for i in comp:
			temp = []
			for j in i:
				temp.append(eval(j))
			plt.plot(size,temp,label=benchmarks[count],alpha=0.6)
			count+=1
		plt.legend()
		plt.xlabel('Size(in MB)')
		plt.ylabel(p)
		# plt.show()
		pdf.savefig()
		plt.clf()
