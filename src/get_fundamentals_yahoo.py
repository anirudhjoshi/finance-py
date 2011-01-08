################################################################################
# Copyright (C)  2010 Ray M. Salem
# http://code.google.com/p/finance-py/
# Distributed under the GPL license Version 3.0 ( See accompanying file 
# License_ or copy at http://code.google.com/p/finance-py/LICENSE)
################################################################################

##
#  Yahoo Finance fundamental data
#  Uses url request
#   reference : http://www.gummy-stuff.org/Yahoo-data.htm
#
## 

## Example Yahoo url to get BP/GS PE
# http://www.download.finance.yahoo.com/d/quotes.csv?s=GS+BP&f=n
# http://www.gummy-stuff.org/Yahoo-data.htm

          
# External libs
import sys
import os
import getopt
import urllib
from scipy import *
from numpy import *


MAX_SYMBOL_QUERY_SIZE = 200;                   
def get_fundamentals(fields, stockListIn):                 
  results = list();
  N = stockListIn.__len__()
  M = N / MAX_SYMBOL_QUERY_SIZE;
#  if __debug__:
#    print N
#    print M    
  for m in range(0,M+1):
    L = min( (m+1)*MAX_SYMBOL_QUERY_SIZE, N)
    stockListP=""
    for index in  range(m*200,L):
      stockListP = stockListP + stockListIn[index]+"+"
    temp = get_fundamentals_prv(fields,stockListP)
    results = results + temp;
    if __debug__ and results.__len__() != stockListIn.__len__():
      print "In(%d)/Out(%d) Sizes do no match." % (stockListIn.__len__(),results.__len__())
  return results
def get_fundamentals_prv(fields, stockListIn):    
  strUrl = "http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=%s" % (stockListIn[:-1],fields)
  
#  if __debug__:
#    print strUrl
  uf = urllib.urlopen(strUrl)
  data1 = uf.read()
  uf.close()
    
  
  data1 = data1.split('\n')
  N = size(data1)-1;
  results = list();
  
  
 
  for index in arange(0,N):
    rr = ""        
    data = data1[index].replace("\r","").split(',')  
    M = size(data); # there is any empty element
    tt = list()
    longEntry=False
    for index in range(0,M):
#      print data[index]
      if(data[index][0] == '\"' and data[index][-1] != '"'):
        rr = rr + data[index].replace('"','')
        longEntry = True;
      elif(longEntry == True):
        rr = rr + data[index].replace('"','')
        if(data[index][0] == '"' and data[index].__len__() == 1):   # handle case where last segment is only '"'
          longEntry = False
          tt.append(rr)                
        elif(data[index][0] != '\"' and data[index][-1] == '"'):
          longEntry = False
          tt.append(rr)        
      else:
        tt.append(data[index])
    #print tt  
    #print longEntry
    results.append(tt)
  
  return results;
             
               
class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
          opts, args = getopt.getopt(argv[1:], "h", ["help"])
        except getopt.error, msg:
          raise Usage(msg)
        if(sys.argv.__len__() < 2):
          print "Function usage is 'fields, ticker list'"
          
        else:
          return get_fundamentals( argv[1], argv[2:] )        
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2        

if __name__ == "__main__":  
  res = main()
  print res                   