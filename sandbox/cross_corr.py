
################################################################################
# Copyright (C)  2010 Ray M. Salem
# http://code.google.com/p/finance-py/
# Distributed under the GPL license Version 3.0 ( See accompanying file 
# License_ or copy at http://code.google.com/p/finance-py/LICENSE)
################################################################################

################################################################################
# Given a list of symbols, this algorithm, will run a cross correlation between 
# every possibly pair, and print to a csv file.
#
#
################################################################################
import sys
sys.path.append("../src/")
sys.path.append("..\src")

from historical_data_obj import * 
 
from scipy import *
from numpy import * 
import csv


##
# Paramaters
# 0--> Close, 1--> Log(price change)) 
dataType = 0
# 0--> pearon, 1--> Spearman
corrType = 0




## Get symbosl
fileName="big.list"
fid = open(fileName, 'r')
reader= csv.reader(fid)
tickers = list()
for row in reader:
  tickers.append(row[0])
#tickers = ['dia','spy','qqqq','gld', 'oil','ge','xom','ceva','mspd','gs','qcom'];
fid.close()

# Get data from yahoo
N=tickers.__len__()
data=list()
index  =0
for symbol in tickers:
  
  data.append( HistoricalDataObj() )
  # Use annual volatility. 
  try:
    data[index].initialize(symbol,365,1,1, 'yahoo');
    data[index].init("logData")
  except:
    print symbol
  index = index +1;

# Run cross correlation
start_index = 1;
ref_index   = 0
results_r     = zeros((N,N))
results_p     = zeros((N,N))

for symbol in tickers:
  
  for index in arange(0, start_index):
    R = min(size(data[ref_index].vClose),size(data[index].vClose));
    
    if(dataType == 0):
      if(corrType == 0):
        temp = stats.pearsonr(data[index].vClose[0:R],data[ref_index].vClose[0:R])
      elif(corrType == 1):
        temp = stats.spearmanr(data[index].vClose[0:R],data[ref_index].vClose[0:R])
    elif(dataType == 1):
      if(corrType == 0):
        temp = stats.pearsonr(data[index].vLdata[0:R],data[ref_index].vLdata[0:R])
      elif(corrType == 1):
        temp = stats.spearmanr(data[index].vLdata[0:R],data[ref_index].vLdata[0:R])            
    
    results_r[ref_index][index] = temp[0]
    results_p[ref_index][index] = temp[1]
    
  ref_index = ref_index +1 
  start_index= start_index +1  
  
  
# print out results  
start_index = 1;
ref_index   = 0 
fid_r = open("r.csv",'w')
fid_p = open("p.csv",'w')
fid_r.write(",")
fid_p.write(",")
for symbol in tickers:
  fid_r.write(symbol + ",");
  fid_p.write(symbol + ",");
fid_r.write(symbol + "\n");
fid_p.write(symbol + "\n");
for symbol in tickers:
  fid_r.write(symbol + ",")
  fid_p.write(symbol + ",")
  for index in arange(0, start_index):  
    fid_r.write(results_r[ref_index][index].__str__() + ",")
    fid_p.write(results_r[ref_index][index].__str__() + ",")
  fid_r.write("\n")
  fid_p.write("\n")
  ref_index = ref_index + 1 
  start_index= start_index + 1    
  
fid_r.close()
fid_p.close()  