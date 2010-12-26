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
                   
def get_fundamentals(fields, stockListIn):                 
  stockListP=""
  for ticker in stockListIn:
    stockListP = stockListP + ticker+"+"
    
  strUrl = "http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=%s" % (stockListP[:-1],fields)
  
  if __debug__:
    print strUrl
  uf = urllib.urlopen(strUrl)
  data1 = uf.read()
  uf.close()
    
  
  data1 = data1.split('\n')
  N = size(data1)-1;
  results = list();
  
  
 
  for index in arange(0,N):
    rr = ""
    #print data1[index]
    data = data1[index].replace("\r","").split(',')
    print data
    M = size(data); # there is any empty element
    tt = list()
    longEntry=False
    for index in range(0,M):
      print data[index]
      if(data[index][0] == '\"' and data[index][-1] != '"'):
        rr = rr + data[index].replace('"','')
        longEntry = True;
      elif(longEntry == True):
        rr = rr + data[index].replace('"','')
        if(data[index][0] != '\"' and data[index][-1] == '"'):
          longEntry = False
          tt.append(rr)        
      else:
        tt.append(data[index])
         
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