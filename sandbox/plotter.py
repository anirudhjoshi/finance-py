################################################################################
# Copyright (C)  2010 Ray M. Salem
# http://code.google.com/p/finance-py/
# Distributed under the GPL license Version 3.0 ( See accompanying file
# License_ or copy at http://code.google.com/p/finance-py/LICENSE)
################################################################################
import sys
from numpy import *
from scipy import *
from datetime import date, timedelta

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick, candlestick2
from matplotlib.ticker import Formatter

sys.path.append("../src/")
sys.path.append("..\src")
import moving_average
import macd

import stochastic_oscillator
from historical_data_obj import *

#
# symbol ticker to be plotted
# daysBack days back for data request
# daysToPlot days to actually plot
#
if (sys.argv.__len__() == 1):
  print "Must provide symbol and days going back.  for example: yhoo 1000"
  exit()
elif(sys.argv.__len__() == 3):
  symbol = sys.argv[1]
  daysBack = int(sys.argv[2])
  daysToPlot =-1
elif(sys.argv.__len__() == 4):
  symbol = sys.argv[1]
  daysBack   = int(sys.argv[2])
  daysToPlot = int(sys.argv[3])
elif(sys.argv.__len__() == 5):
  symbol = sys.argv[1]
  daysBack   = int(sys.argv[2])
  daysToPlot = int(sys.argv[3])
  resolution = int(sys.argv[4])  
else:
  print "Must provide symbol and days going back.  for example: yhoo 1000 900 "
  #exit()
  daysBack = 150;
  daysToPlot = 150;
  symbol = "gs"




data = HistoricalDataObj()
data.initialize( symbol,daysBack, 1, resolution, 'google');
N = size(data.vClose);
if(daysToPlot == -1):
  daysToPlot = -1*N
elif(N <= daysToPlot):
  print "Error Days to plot must be less the days back"
  exit()
else:
  daysToPlot = -1*daysToPlot


class MyFormatter(Formatter):
    def __init__(self, dates, fmt='%Y-%m-%d'):
        self.dates = dates
        self.fmt = fmt

    def __call__(self, x, pos=0):
        'Return the label for time x at position pos'
        ind = int(round(x))
        if ind>=len(self.dates) or ind<0: return ''

        return self.dates[ind].strftime(self.fmt)

formatter=  MyFormatter(data.vDate[daysToPlot:])


[macdOut, ema, divergence] = macd.macd(data.vOpen, 5,10, 4)
[per_k, per_d] = stochastic_oscillator.stoc_osc(data.vHigh, data.vLow, data.vClose,15,5,5,"ema")

plt.figure(1)
ax1 = plt.subplot('311')

candlestick2(ax1, data.vOpen[daysToPlot:],data.vClose[daysToPlot:],data.vHigh[daysToPlot:],data.vLow[daysToPlot:], width=0.6)
# MACD
ax2 = plt.subplot('312')
ax2.plot(macdOut[daysToPlot:])
ax2.plot( ema[daysToPlot:])
ax2.stem(arange(-1*daysToPlot), divergence[daysToPlot:])
# Stochastic Oscillator.
ax3 = plt.subplot('313')
ax3.plot(per_k[daysToPlot:], color="red")
ax3.plot(per_d[daysToPlot:], color='darkviolet')
ax3.axhline(70, color="grey")
ax3.axhline(30, color="grey")
ax3.set_ylim(0, 100)
ax3.set_yticks([30,70])


ax1.set_title(symbol)
for ax in ax1, ax2, ax3:#, ax1t:
    if ax!=ax3:
        for label in ax.get_xticklabels():
            label.set_visible(False)
    else:
        for label in ax.get_xticklabels():
            label.set_rotation(-30)
            label.set_horizontalalignment('center')

    ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
    ax.xaxis.set_major_formatter(formatter)
plt.show()
