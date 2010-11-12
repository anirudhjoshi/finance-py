################################################################################
# Copyright (C)  2010 Ray M. Salem
# http://code.google.com/p/finance-py/
# Distributed under the GPL license Version 3.0 ( See accompanying file 
# License_ or copy at http://code.google.com/p/finance-py/LICENSE)
################################################################################

from numpy import *
from scipy import *


from matplotlib.finance import quotes_historical_yahoo
import sys
from datetime import date,timedelta

import matplotlib.pyplot as plt

import moving_average
import macd
import candle_stick
from historical_data_obj import *
################################################################################
# Main Routine
################################################################################
#1st thing get some data and creat our object
daysBack = 150;
symbol = 'gs'
obj = HistoricalDataObj()
obj.initialize( symbol,daysBack, 1, 1, 'yahoo'); 





fig = plt.figure()
ax1 = fig.add_subplot(211)
candle_stick.candleSticks(obj.quotes, ax1)
plt.show()


