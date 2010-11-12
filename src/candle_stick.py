################################################################################
# Copyright (C)  2010 Ray M. Salem
# http://code.google.com/p/finance-py/
# Distributed under the GPL license Version 3.0 ( See accompanying file 
# License_ or copy at http://code.google.com/p/finance-py/LICENSE)
################################################################################

#!/usr/bin/env python
################################################################################
import sys
from pylab import *
from matplotlib.dates import  DateFormatter, WeekdayLocator, HourLocator, \
     DayLocator, MONDAY
from matplotlib.finance import quotes_historical_yahoo, candlestick,\
     plot_day_summary, candlestick2

####
print ( "obsolete function")
####

def candleSticks(quotes, ax):
    mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
    alldays    = DayLocator()               # minor ticks on the days
    weekFormatter = DateFormatter('%b %d')  # Eg, Jan 12
    dayFormatter = DateFormatter('%d')      # Eg, 12

    if not quotes:
        raise SystemExit


#    ax.xaxis.set_major_locator(mondays)
#    ax.xaxis.set_minor_locator(alldays)
#    ax.xaxis.set_major_formatter(weekFormatter)
    #ax.xaxis.set_minor_formatter(dayFormatter)

    #plot_day_summary(ax, quotes, ticksize=3)
    candlestick(ax, quotes, width=0.6)

    ax.xaxis_date()
#    ax.autoscale_view()
#    setp( gca().get_xticklabels(), rotation=45, horizontalalignment='right')

#    show()
