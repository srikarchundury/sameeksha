import os
import img2pdf
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

limit = 35

path = 'C://Users//srama//Documents//GitHub//Sameeksha//Results//wordcount_tungsten_studies//'
benchmarks = os.listdir(path)

with PdfPages('./Tool_Output/'+"PinTool_Results"+'.pdf') as pdf:
	for b in benchmarks:
		for f in os.listdir(path+b):
			print(b,f)
			file = open(path+b+'//'+f)
			data = dict()
			colors=['green', 'blue', 'cyan', 'orange', 'black', 'red']
			absorb=False
			count=0

			for line in file:
				count+=1
				if line.startswith('*'):
					absorb = False
					break
				if(absorb):
					line = line[:-1]
					if(not line.startswith('#')):
						temp = line.split(' ') #.replace(' ',''))
						temp[1] = '/'
						temp = ' '.join(temp)
						temp = temp.replace(' ','')
						temp = temp.split('/')
						data[int(temp[1])]=temp[0]
				if line.startswith('# opcode '):
					absorb = True

			val = list(data.keys())
			val.sort(reverse=True)

			val = val[:limit]
			n = len(val)
			y = [i for i in range(0,n)]
			headers = [data[val[i]] for i in range(0,n)]

			len(list(data.values()))
			list(data.values())[:limit]


			plt.clf()
			plt.bar(y, val, align='center', alpha=0.5, color=colors, edgecolor='black', width=1.0)
			plt.xticks(y, headers,rotation=90)
			plt.title(b+'_'+f)
			plt.tight_layout()
			pdf.savefig()
			# plt.show()
			file.close()
