
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
daysBack = 1500;
obj = HistoricalDataObj();
date1 = date.today() - timedelta(days=daysBack)
# end
date2 = date.today()
obj.initialize("spy",date1,date2)

ma200 = moving_average.ma(obj.vClose, 200)

#candle_stick.candleSticks(obj.quotes)
plt.plot(obj.vClose);
plt.grid()
plt.hold(True);
plt.plot(ma200);
plt.show()


