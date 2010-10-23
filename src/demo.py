
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



ma200 = moving_average.ma(obj.vClose, 200)

fig = plt.figure()

ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

candle_stick.candleSticks(obj.quotes, ax1)
ax2.plot(obj.vClose);
ax2.grid()
ax2.hold(True);
ax2.plot(ma200);
plt.show()


