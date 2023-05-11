import os
import img2pdf
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

limit = 35

path = 'C://Users//srama//Documents//GitHub//Sameeksha//PIN//Data//'
benchmarks = os.listdir(path)

with PdfPages("PinTool_Instr"+'.pdf') as pdf:
	for h in ['*isa-ext-BASE','MOV','*mem-read-8','CMP','*mem-read-4','*stack-read','*mem-write-8','JNZ','*mem-write-1','JZ','TEST','*stack-write','ADD','STOSB','*mem-write-4','INC','JNB','*mem-read-1','SUB']:
		print(h)
		head2 = []
		for b in benchmarks:
			head2.append(b)
			bData = []

			print('\t',b)
			for f in os.listdir(path+b):
				file = open(path+b+'//'+f)
				data = dict()
				colors=['green', 'blue', 'cyan', 'orange', 'black', 'red']
				absorb=False
				count=0

				for line in file:
					count+=1
					if line.startswith('# END_DYNAMIC_STATS'):
						absorb = False
					if(absorb):
						line = line[:-1]
						if(not line.startswith('#')):
							# print(line)
							temp = line.split(' ') #.replace(' ',''))
							temp[1] = '/'
							temp = ' '.join(temp)
							temp = temp.replace(' ','')
							temp = temp.split('/')
							if temp[0] not in data.keys():
								data[temp[0]]=0
							data[temp[0]]+=int(temp[1])
					if line.startswith('# $dynamic-counts\n'):
						absorb = True

				data2 = dict()
				for i in list(data.keys()):
					data2[data[i]] = i
				# data = data2

				val = list(data2.keys())
				val.sort(reverse=True)


				n = len(val)
				y = [i for i in range(0,n)]
				# y = [1,10,20,30,40,50]
				headers = [data2[val[i]] for i in range(0,n)]

				bData.append(data[h])

			y = []
			for o in os.listdir(path+b):
				y.append(int(o[:2]))
			plt.plot(y,bData)
		plt.legend(benchmarks)
		plt.title(h)
		# plt.xticks(y, headers,rotation=90)
		plt.tight_layout()
		pdf.savefig()
		plt.clf()
			# break

# plt.show()
# plt.clf()
