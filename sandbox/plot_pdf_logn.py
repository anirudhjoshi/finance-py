################################################################################
# Copyright (C)  2010 Ray M. Salem
# http://code.google.com/p/finance-py/
# Distributed under the GPL license Version 3.0 ( See accompanying file 
# License_ or copy at http://code.google.com/p/finance-py/LICENSE)
################################################################################
################################################################################
# Author - Ray Salem
# Description - Given a stock, it will plot the distributions of change and stock price
#                versus the normal and log-normal distribution. 
# Creation date
# History
# References
#
#
#
# References
#            - Normal Distribution - http://mathworld.wolfram.com/NormalDistribution.html
#            - log normal dist     - http://en.wikipedia.org/wiki/Log-normal_distribution

## include source path
import sys
sys.path.append("../src/")

from historical_data_obj import * 

import matplotlib.pyplot as plt

Nsmpl = 365;

data = HistoricalDataObj()
data.initialize("gs",365);


## lets look at price chages (prev-close)/close
x =( data.vClose[1:] - data.vClose[:-1] ) / data.vClose[1:] * 100



s = var(x);
u = mean(x);
z = arange(-6,6, 0.01);
plt.figure(1);
plt.hist(x,100, normed=True);
plt.plot(z,1.0/sqrt(2.0*pi*s) * exp(-(z-u)**2/(2*s)),'r')
plt.title('Distribution of price changes (%)')

## Next example take log of current day and previous day closes


x = data.vClose[1:] / data.vClose[:-1];
y = log(x);
Nsmpl = 252
s = std(y) * 1/sqrt(1.0/Nsmpl);
print(s * 100)

plt.figure(2)
z = arange(0,200,1);
plt.hist(y, 100, normed = True)
plt.title("Normal distribution of Y");



sig = var(y);
mu  = mean(y)
z=arange(0.75,1.25,sig)
Fx = 1.0/(z*sqrt(2.0*pi*sig)) * exp(-(log(z)-mu)**2/(2*sig));

plt.figure(3)
plt.hist(x, 100, normed = True)
plt.hold(True);
plt.title("Log Normal distribution of x");


plt.plot(z, Fx, 'r')


plt.figure(4)
plt.plot(data.vClose);
plt.plot(data.vClose[0] * exp(mu * arange(0,Nsmpl)))

plt.show()
