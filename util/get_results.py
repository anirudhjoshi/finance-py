#! /usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rsalem
#
# Created:     13/07/2011
# Copyright:   (c) RMS investment 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
import xml.dom.minidom
import csv

workPath = '.'
if (sys.argv.__len__() == 3):
	workPath = sys.argv[1];
	fileName = sys.argv[2];	
else:
	print "Incorrect parametesr provided"
	exiit()


testNameList = list();
f = open(workPath + "//" + fileName, 'r') 
reader = csv.reader(f)
	
rowIndex =  0;	
for row in reader:		
	if(rowIndex  != 0):					
		testNameList.append(row[0])
	rowIndex = rowIndex +1;
f.close()


docOut = xml.dom.minidom.Document()
cc1 = docOut.createComment("license:License")
cc2 = docOut.createComment("strictly confidential. Propietary Information")
docOut.appendChild(cc1)
docOut.appendChild(cc2)
top = docOut.createElement("Results")
docOut.appendChild(top)

for testCase in testNameList:	
	workPathTemp = workPath + "//" + testCase;
	doc = xml.dom.minidom.parse(workPathTemp  + "//results.xml")
	final = doc.getElementsByTagName("final")[0]
	final.setAttribute("name", testCase);
	final.setAttribute("id", str(testCase) )
	final.setIdAttribute("id")
	v_attr = final.attributes
	top.appendChild(final);
	print final.toprettyxml()
	for index in range(0, v_attr.length):
		v_attr.values()[index].name
		v_attr.values()[index].value
		
f = open(workPath + "//" + "results.xml",'w')
docOut.writexml(f, addindent="\t",newl="\n");
f.close()		