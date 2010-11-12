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

sys.path.append("../src/");
import moving_average
import macd

import stochastic_oscillator
from historical_data_obj import *

class PlotterFormateter(Formatter):
  def __init__(self, dates, fmt="%Y-%m-%d"):
    self.dates = dates;
    self.fmt = fmt;
  def __call__(self,x,pos = 0):
    ind = int(round(x))
    if ind > len(self.dates) or ind < 0:
      return ''

    return self.dates[ind].strftime(self.fmt)

if (sys.argv.__len__() == 1):
  print "Must provide symbol and days going back.  for example: yhoo 1000"
  print "Output format is data, open, close, high, low, volume"
  exit()
else:
  symbol = sys.argv[1]
  daysBack = int(sys.argv[2])

data = HistoricalDataObj()
data.initialize( symbol,daysBack, 1, 1, 'yahoo'); 
N = size(data);

macdOut, ema, divergence = macd.macd(data.vOpen, 5,10, 4)

plt.rc('axes', grid=True)
plt.rc('grid', color='0.75', linestyle='-', linewidth=0.5)

textsize = 9
#left, bottom, width, height
left, width = 0.1, 0.8
rect1 = [left, 0.5, width, 0.4]
rect2 = [left, 0.3, width, 0.2]
rect3 = [left, 0.1, width, 0.2]


fig = plt.figure(facecolor='white')
axescolor  = '#f6f6f6'  # the axies background color

ax1  = fig.add_axes(rect1, axisbg=axescolor)
ax1t = ax1.twinx()
ax2  = fig.add_axes(rect2, axisbg=axescolor, sharex=ax1)
ax3  = fig.add_axes(rect3, axisbg=axescolor, sharex=ax1)



### plot stochastic oscillator
[per_k, per_d] = stochastic_oscillator.stoc_osc(data.vHigh, data.vLow, data.vClose,15,5,5,"ema")

fillcolor = 'darkgoldenrod'
"""
list of colors support by html
http://plantphys.info/demo/Colors.html
"""

# Data
#ax1.plot(arange(N),  data.vClose)
candlestick(ax1, data.quotes, width=0.6)
ax1t.fill_between(data.vDate, data.vVolume, 0, color='orange')
ax1t.set_ylim(0, 5 * max(data.vVolume))
# MACD
ax2.plot(data.vDate, macdOut)
ax2.plot(data.vDate, ema)
ax2.stem(data.vDate, divergence)
# Stochastic Oscillator.
ax3.plot(data.vDate, per_k, color=fillcolor)
ax3.plot(data.vDate, per_d, color='darkviolet')
ax3.axhline(70, color=fillcolor)
ax3.axhline(30, color=fillcolor)
ax3.set_ylim(0, 100)
ax3.set_yticks([30,70])

# fill over sold and over
#ax3.fill_between(data.vDate, per_k, 70, where=(per_k>=70), facecolor=fillcolor, edgecolor=fillcolor)
#ax3.fill_between(data.vDate, per_k, 30, where=(per_k<=30), facecolor=fillcolor, edgecolor=fillcolor)


#ax3.set_title('%s daily'%symbol)


for ax in ax1, ax2, ax3, ax1t:
    if ax!=ax3:
        for label in ax.get_xticklabels():
            label.set_visible(False)
    else:
        for label in ax.get_xticklabels():
            label.set_rotation(30)
            label.set_horizontalalignment('right')

    ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')

class MyLocator(mticker.MaxNLocator):
    def __init__(self, *args, **kwargs):
        mticker.MaxNLocator.__init__(self, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        return mticker.MaxNLocator.__call__(self, *args, **kwargs)

# at most 5 ticks, pruning the upper and lower so they don't overlap
# with other ticks
#ax2.yaxis.set_major_locator(mticker.MaxNLocator(5, prune='both'))
#ax3.yaxis.set_major_locator(mticker.MaxNLocator(5, prune='both'))

#ax2.yaxis.set_major_locator(MyLocator(5, prune='both'))
#ax3.yaxis.set_major_locator(MyLocator(5, prune='both'))

plt.show()
