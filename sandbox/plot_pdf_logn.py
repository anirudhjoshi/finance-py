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


## include source path
import sys
sys.path.append("../src.")

from historical_data_obj import * 

import matplotlib.pyplot as plt

data = HistoricalDataObj()
data.initialize('gs',365);


x =( data.vClose[1:] - data.vClose[:-1] ) / data.vClose[1:] * 100



s = var(x);
u = mean(x);
z = arange(-3,3, 0.01);

plt.hist(x,100, normed=True);
plt.plot(z,1.0/sqrt(2.0*pi*s) * exp(-(z-u)**2/(2*s)),'r')



s = var(log(data.vClose));
u = mean(log(data.vClose));

plt.figure()
z = arange(0,200,1);
plt.hist(data.vClose, 100, normed = True)
plt.plot(z,1.0/(z*sqrt(2.0*pi*s)) * exp(-(log(z)-u)**2/(2*s)),'r')




# lets the random generator
#plt.hist(randn((1e6)),1000,normed=True)
#plt.plot(z,1.0/sqrt(2.0*pi*s) * exp(-(z-u)**2/(2*s)),'r')
#plt.show()





plt.show()
