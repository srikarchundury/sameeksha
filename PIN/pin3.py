import os
import img2pdf
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

limit = 35

path = 'C://Users//srama//Documents//GitHub//Sameeksha//PIN//Data//'
benchmarks = os.listdir(path)

# with PdfPages("PinTool_Results"+'.pdf') as pdf:
for b in benchmarks:
	# out = list([[]]*limit)
	out = []
	for l in range(0,limit):
		out.append([])
	for f in os.listdir(path+b):
		print(b,f)
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
		data = data2

		val = list(data.keys())
		val.sort(reverse=True)

		val = val[:limit]
		n = len(val)
		y = [i for i in range(0,n)]
		# y = [1,10,20,30,40,50]
		headers = [data[val[i]] for i in range(0,n)]

		len(list(data.values()))
		list(data.values())[:limit]

		# # plt.bar(y, val, align='center', alpha=0.5, color=colors, edgecolor='black', width=1.0)
		# plt.plot(y, val)
		# # file.close()
		# plt.legend(os.listdir(path+b))
		# plt.title(b)
		# plt.xticks(y, headers,rotation=90)
		# plt.tight_layout()
		# pdf.savefig()
		# plt.clf()
		for i in range(0,limit):
			out[i].append(headers[i]) #,val[i]))

	# print(out)
	# break
	f1=open('out.csv','a')
	f1.write(b+'\n\n')
	f1.write('\t'.join(os.listdir(path+b))+'\n')

	for s in out:
		f1.write('\t'.join(s))
		f1.write('\n')
	f1.write('\n')
	f1.write('\n\n')
	f1.close()


# plt.show()
# plt.clf()
