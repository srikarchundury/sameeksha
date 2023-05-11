import os
import img2pdf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys
import string

name=sys.argv[1].split('.')[0]
print("name="+name)

path = "Tool_Data/"
file = open(path+sys.argv[1],'r')
data = []

headers = []
h = 1

for i in file:
	s=i[:-1]
	data.append(s.split('\t'))
	print(s.split('\t'))
file.close()

headers = data[0]
data = data[1:-1]

headers

n = len(headers)
y = [i for i in range(0,n)]

with PdfPages('./Tool_Output/'+name+'.pdf') as pdf:
	for i in data:
		title = i[0]
		val = i[1:]
		# OFF = i[6:]

		print(title,val)
		for num in range(0,n):
			val[num] = eval(val[num])

		# print(y)
		# break

		plt.clf()

		plt.bar(y, val, align='center', alpha=0.5)
		plt.xticks(y, headers,rotation=90)
		plt.ylabel(title)
		plt.title(name)


		# plt.bar(y,ON,label="Tungsten ON")
		# plt.plot(y,OFF,label="Tungsten OFF")
		# plt.xlabel('Benchmark Size', fontsize=14)
		# plt.ylabel(title, fontsize=14)
		# plt.xticks([0,1,2,3,4],['1B','2B','3B','4B','5B'])
		# plt.grid(axis='y', linestyle='-')
		# plt.legend()
		plt.tight_layout()
		pdf.savefig()
