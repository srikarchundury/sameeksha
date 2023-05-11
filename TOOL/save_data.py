import pickle
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

with open('data.pickle', 'wb') as handle:
    pickle.dump(PlotData, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('data.pickle', 'rb') as handle:
    b = pickle.load(handle)

print("Sanity Check Pass = ",PlotData == b)
