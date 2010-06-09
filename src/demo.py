################################################################################
#                Copyright (c) 2009 Omni Wireless Communication Inc
#       All rights are reserved. Reproduction in whole or in parts is
#       prohibited without the written consent of the copyright owner.
#
#               Address:  3755 avocado Blvd
#                         Suite 434
#                         La Mesa, Ca, 91941
#
#               Tel:    619-378-6000
#               Web:    www.omniwcomm.net
#
################################################################################
#   Demo routine emcompassing other routines,
#
#
#
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


