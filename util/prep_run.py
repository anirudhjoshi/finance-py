from numpy import *
from scipy import *
import csv
from xml.dom.minidom import Document

with open('example.csv', 'r') as f:
	reader = csv.reader(f)
	rowIndex =  0;
	for row in reader:
		if(rowIndex  == 0):
			header = row#.split(',')
			N = size(header)
		else:
			cols = row#.split(',')
			print cols[0]
			
			# Create the minidom document
			doc = Document()
			cc1 = doc.createComment("license:RMS Investment 2011")
			cc2 = doc.createComment("strictly confidential. Propietary Information")
			doc.appendChild(cc1)
			doc.appendChild(cc2)
			# Create the <main> base element
			top = doc.createElement("dvg_sns")
			top.setAttribute("testName", cols[0])
			doc.appendChild(top)
			for index in range(1,N):
				print "\t%s = %s" % ( header[index], cols[index])
				parameter = doc.createElement("parameter")
				parameter.setAttribute("name", header[index])
				parameter.setAttribute("value", cols[index])
				top.appendChild(parameter)
			
			f = open(cols[0] + ".xml",'w');
			doc.writexml(f);
			f.close()
		
		
		
		
			
		rowIndex = rowIndex + 1
		
		

	f.close()
	