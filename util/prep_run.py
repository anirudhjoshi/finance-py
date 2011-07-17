from numpy import *
from scipy import *
import csv
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
			for index in range(1,N):
				print "%s = %s" % ( header[index], cols[index])
				
		
		
		
		
			
		rowIndex = rowIndex + 1
		
		

	f.close()
	