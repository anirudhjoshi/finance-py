
################################################################################
# Copyright (C)  2010 Ray M. Salem
# http://code.google.com/p/finance-py/
# Distributed under the GPL license Version 3.0 ( See accompanying file 
# License_ or copy at http://code.google.com/p/finance-py/LICENSE)
################################################################################




from historical_data_obj import * 
 
from scipy import *
from numpy import * 




tickers = ['gs','qcom','dia','spy','qqqq','gld', 'oil','ge','xom','ceva','mspd'];
N=tickers.__len__()
data=list()
index  =0
for symbol in tickers:
  
  data.append( HistoricalDataObj() )
  # Use annual volatility. 
  data[index].initialize(symbol,365,1,1, 'yahoo');
  index = index +1;


start_index = 1;
ref_index   = 0
results     = zeros((11,11))

for symbol in tickers:
  
  for index in arange(start_index, N):
    R = min(size(data[ref_index].vClose),size(data[index].vClose));
    temp = stats.corrcoef(data[index].vClose[0:R],data[ref_index].vClose[0:R])
    results[ref_index][index] = temp[0][1]
  ref_index = ref_index +1 
  start_index= start_index +1