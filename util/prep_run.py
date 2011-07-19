from numpy import *
from scipy import *
import csv
import sys
import os
from xml.dom.minidom import Document

##
#	1 -argument
#		specify input file name
# 	2- argument 
#		* path
#		* input file name
#
##

# True --> each test case will get a unique directory, but output xml will allways be called parameters.xml
individualTestDir = True;
workPath = ""
if (sys.argv.__len__() == 2):
	fileName = sys.argv[1];	
elif (sys.argv.__len__() == 3):
	workPath = sys.argv[1];
	fileName = sys.argv[2];	
else:
  print "Must provide symbol and days going back.  for example: yhoo 1000"
  exit()

with open(workPath + "//" + fileName, 'r') as f:
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
			if(individualTestDir  == True):
				workPath = workPath + cols[0] 
				os.mkdir(workPath)
			doc.appendChild(top)
			for index in range(1,N):
				print "\t%s = %s" % ( header[index], cols[index])
				parameter = doc.createElement("parameter")
				parameter.setAttribute("name", header[index])
				parameter.setAttribute("value", cols[index])
				top.appendChild(parameter)
			if(individualTestDir ==True):
				f = open(workPath + "//parameters.xml",'w');
			else:
				f = open(workPath + "//" + cols[0] + ".xml",'w');
			doc.writexml(f);
			f.close()
		
		
		
		
			
		rowIndex = rowIndex + 1
		
		

	f.close()
	