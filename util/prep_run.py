from numpy import *
from scipy import *
import csv
import sys
import os
import shutil
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
executableName = "python c:\\owc\\dvg_study\\src\\backtest\\tester.py"
workPath = ""
if (sys.argv.__len__() == 2):
	fileName = sys.argv[1];	
elif (sys.argv.__len__() == 3):
	workPath = sys.argv[1];
	fileName = sys.argv[2];	
else:
  print "Incorrect parametesr provided"
  exit()

with open(workPath + "//" + fileName, 'r') as f:
	reader = csv.reader(f)
	rowIndex =  0;
	id = 0;
	
	fExe = open(workPath + "//cmd", 'w');
	for row in reader:
		if(rowIndex  == 0):
			header = row#.split(',')
			N = size(header)
		else:
			cols = row#.split(',')
			print cols[0]
			
			# Create the minidom document
			doc = Document()
			cc1 = doc.createComment("license:")
			cc2 = doc.createComment("strictly confidential. Propietary Information")
			doc.appendChild(cc1)
			doc.appendChild(cc2)
			# Create the <main> base element
			top = doc.createElement("dvg_sns")
			doc.appendChild(top)
			top.setAttribute("id", str(id) )
			top.setIdAttribute("id")
			id = id + 1;
			top.setAttribute("testName", cols[0])
			if(individualTestDir  == True):
				workPathTemp = workPath + cols[0] 
				shutil.rmtree(workPathTemp, True)		
				os.mkdir(workPathTemp)
			else:
				workPathTemp = workPath
			
			for index in range(1,N):
				print "\t%s = %s" % ( header[index], cols[index])
				parameter = doc.createElement("parameter")
				parameter.setAttribute("name", header[index])
				parameter.setAttribute("value", cols[index])
				top.appendChild(parameter)
			if(individualTestDir ==True):
				f = open(workPathTemp + "//parameters.xml",'w');
				fExe.write(executableName + " " + workPathTemp +" parameters.xml\n");
			else:
				f = open(workPathTemp + "//" + cols[0] + ".xml",'w');
				fExe.write( executableName + " " + workPathTemp +" " +  cols[0] + ".xml\n");
			doc.writexml(f);
			f.close()
		
		
			
		rowIndex = rowIndex + 1
		
		

	fExe.close()
	