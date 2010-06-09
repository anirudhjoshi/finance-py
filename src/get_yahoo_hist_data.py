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

#!/usr/bin/env python
from matplotlib.finance import quotes_historical_yahoo
import sys
from datetime import date,timedelta


################################################################################
# Get historical data
################################################################################
def get(symbol, daysBack, fileWrite):
    date1 = date.today() - timedelta(days=daysBack)
    # end
    date2 = date.today()

    quotes = quotes_historical_yahoo(
        symbol, date1, date2)


    if(fileWrite == 1):
        f = open(symbol + ".csv", 'w')
        for line in quotes:
          for val in line:
            f.write(str(val))
            f.write(',')
          f.write('\n')

        f.close()
################################################################################

if (sys.argv.__len__() ==1):
  print "Propietary Module of Omni Wireless Communications Inc. "
  print "Version 0.0.1"
  print "Must provide symbol and days going back.  for example: yhoo 1000"
  print "Output format is data, open, close, high, low, volume"  
  exit()
else:
  symbol   = sys.argv[1]
  daysBack = int(sys.argv[2])




get(symbol, daysBack, 1)
