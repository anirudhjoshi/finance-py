################################################################################
#				Copyright (c) 2009 Omni Wireless Communication Inc
#	   All rights are reserved. Reproduction in whole or in parts is
#	   prohibited without the written consent of the copyright owner.
#
#			   Address:  3755 avocado Blvd
#						 Suite 434
#						 La Mesa, Ca, 91941
#
#			   Tel:	619-378-6000
#			   Web:	www.omniwcomm.net
#
################################################################################
#!/usr/bin/env python
import sys
from pylab import *
from matplotlib.dates import  DateFormatter, WeekdayLocator, HourLocator, \
     DayLocator, MONDAY, timezone
from matplotlib.finance import quotes_historical_yahoo, candlestick,\
     plot_day_summary, candlestick2

import datetime
from datetime import date,timedelta

def candleSticks(quotes):
    mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
    alldays    = DayLocator()              # minor ticks on the days
    weekFormatter = DateFormatter('%b %d')  # Eg, Jan 12
    dayFormatter = DateFormatter('%d')      # Eg, 12

    if not quotes:
        raise SystemExit

    fig = figure()
    fig.subplots_adjust(bottom=0.2)
    ax = fig.add_subplot(111)
    ax.xaxis.set_major_locator(mondays)
    ax.xaxis.set_minor_locator(alldays)
    ax.xaxis.set_major_formatter(weekFormatter)
    #ax.xaxis.set_minor_formatter(dayFormatter)

    #plot_day_summary(ax, quotes, ticksize=3)
    candlestick(ax, quotes, width=0.6)

    ax.xaxis_date()
    ax.autoscale_view()
    setp( gca().get_xticklabels(), rotation=45, horizontalalignment='right')

    show()