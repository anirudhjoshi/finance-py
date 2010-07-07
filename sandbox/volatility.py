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
sys.path.append("../src/")

from historical_data_obj import * 

import matplotlib.pyplot as plt

data = HistoricalDataObj()
data.initialize('gs',365);

#  current minus the   previous
delta  = data.vClose[1:] - data.vClose[:-1] ;
deltaP = delta / data.vClose[1:] * 100;
deltaLn = log(data.vClose[1:] /data.vClose[:-1] );
v = std(deltaLn) ;
#there are 252 trading days in any given year
v2 = v / sqrt(1.0/252.0);
print(v)  * 100
print(v2) * 100



plt.hist(deltaLn)

plt.show()
