##
#  Study template
#  A study is a frame work for scanning for certian stocks, based on
#   certian criteria. It is composed of the following modules
#   (a) the study or studies of interest
#   (b) data feed providing the proper data, being either spot price,
#       historical data, intra-data  
#       Where the data can be stock prices, options, futures....
#
##

import sys
sys.path.append("../src/")

from historical_data_obj import * 
import matplotlib.pyplot as plt

from ma_cross import *


data = HistoricalDataObj()




# first step provide a list of symbols or an index
#  other studies could be based on indices S&P, Dow Jones and Nasdaq
symbols = ["gs", "qcom", "bp", "mmm"]


# For each symbol run the analysis 
#
for symbol in symbols:
    data.initialize(symbol,600);
    maCross(data, 50);
