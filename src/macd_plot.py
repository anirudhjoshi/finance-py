
from numpy import *
from scipy import *

import moving_average
from matplotlib.finance import quotes_historical_yahoo
import sys
from datetime import date, timedelta

import matplotlib.pyplot as plt

import macd

if (sys.argv.__len__() == 1):
  print "Must provide symbol and days going back.  for example: yhoo 1000"
  print "Output format is data, open, close, high, low, volume"
  exit()
else:
  symbol = sys.argv[1]
  daysBack = int(sys.argv[2])


date1 = date.today() - timedelta(days=daysBack)
# end
date2 = date.today()

#  Format of quotes (d, open, close, high, low, volume)
quotes = quotes_historical_yahoo(
    symbol, date1, date2)

N = quotes.__len__();
vOpen = zeros(N)
vClose = zeros(N)
index = 0;
for lines in quotes:#arange(0,N):
    vOpen[index] = lines [1];
    vClose[index] = lines [2];

    index = index + 1;

macdOut, ema, divergence = macd.macd(vOpen, 26, 12, 9)

plt.subplot(2, 1, 1)
plt.plot(vClose);
plt.hold(True)
plt.grid()
plt.subplot(2, 1, 2)
plt.grid()
plt.plot(macdOut, 'k')
plt.plot(ema, 'g')
plt.stem(arange(0, N), divergence)
plt.show()
