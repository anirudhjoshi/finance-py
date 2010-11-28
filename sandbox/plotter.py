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

if (sys.argv.__len__() == 1):
  print "Must provide symbol and days going back.  for example: yhoo 1000"
  exit()
else:
  symbol = sys.argv[1]
  daysBack = int(sys.argv[2])




data = HistoricalDataObj()
data.initialize( symbol,daysBack, 1, 1, 'yahoo'); 
N = size(data.vClose);


class MyFormatter(Formatter):
    def __init__(self, dates, fmt='%Y-%m-%d'):
        self.dates = dates
        self.fmt = fmt

    def __call__(self, x, pos=0):
        'Return the label for time x at position pos'
        ind = int(round(x))
        if ind>=len(self.dates) or ind<0: return ''

        return self.dates[ind].strftime(self.fmt)

formatter=  MyFormatter(data.vDate)        


[macdOut, ema, divergence] = macd.macd(data.vOpen, 5,10, 4)
[per_k, per_d] = stochastic_oscillator.stoc_osc(data.vHigh, data.vLow, data.vClose,15,5,5,"ema")

plt.figure(1)
ax1 = plt.subplot('311')
#ax1t =ax1.twinx()
candlestick2(ax1, data.vOpen,data.vClose,data.vHigh,data.vLow, width=0.6)
# MACD
ax2 = plt.subplot('312')
ax2.plot(macdOut)
ax2.plot( ema)
ax2.stem(arange(N), divergence)
# Stochastic Oscillator.
ax3 = plt.subplot('313')
ax3.plot(per_k, color="red")
ax3.plot(per_d, color='darkviolet')
#ax3.axhline(70, color=fillcolor)   
#ax3.axhline(30, color=fillcolor)
ax3.set_ylim(0, 100)
ax3.set_yticks([30,70])
ax3.xaxis.set_major_formatter(formatter)

#ax1.autoscale_view()
#ax1t.fill_between(data.vDate, data.vVolume, 0, color='orange')
#ax1t.set_ylim(0, 5 * max(data.vVolume))





# fill over sold and bought
#ax3.fill_between(data.vDate, per_k, 70, where=(per_k>=70), facecolor=fillcolor, edgecolor=fillcolor)
#ax3.fill_between(data.vDate, per_k, 30, where=(per_k<=30), facecolor=fillcolor, edgecolor=fillcolor)

#formatter = PlotterFormateter(data.vDate)
#ax1.xaxis.PlotterFormateter(formatter)
ax1.set_title(symbol)
#plt.autofmt_xdate()



for ax in ax1, ax2, ax3:#, ax1t:
    if ax!=ax3:
        for label in ax.get_xticklabels():
            label.set_visible(False)
    else:
        for label in ax.get_xticklabels():
            label.set_rotation(-30)
            #label.set_horizontalalignment('center')

    ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')

#class MyLocator(mticker.MaxNLocator):
#    def __init__(self, *args, **kwargs):
#        mticker.MaxNLocator.__init__(self, *args, **kwargs)
#
#    def __call__(self, *args, **kwargs):
#        return mticker.MaxNLocator.__call__(self, *args, **kwargs)

# at most 5 ticks, pruning the upper and lower so they don't overlap
# with other ticks
#ax2.yaxis.set_major_locator(mticker.MaxNLocator(5, prune='both'))
#ax3.yaxis.set_major_locator(mticker.MaxNLocator(5, prune='both'))
#ax2.yaxis.set_major_locator(MyLocator(5, prune='both'))
#ax3.yaxis.set_major_locator(MyLocator(5, prune='both'))

plt.show()
