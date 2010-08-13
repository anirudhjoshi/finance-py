# References
# - http://www.hoadley.net/options/bs.htm
# - http://en.wikipedia.org/wiki/Binomial_options_pricing_model
# - http://en.wikipedia.org/wiki/Log-normal_distribution


# Notes
#  - Original author of BOPM is  "Cox, Ross and Rubinstein "
#  - volatility is equal to variance, but is express as a percentage. 
# 
#
#
#




from numpy import *
from scipy import *
import sys
sys.path.append("../src/")

from historical_data_obj import * 
from volatility import *
from black_scholes_model import *
import bopm
data = HistoricalDataObj()
# Use annual volatility. 
data.initialize("cat",365,1,1, 'yahoo'); 


spotPrice = data.vClose[-1:];
strikePrice =70;
vola = volatility(data.vClose, 365);
daysToExp = 6;
riskFreeRate = 0.1;

bopmVal = bopm.bopm(spotPrice, strikePrice, vola, daysToExp, riskFreeRate)
print bopmVal;


bsmVal  = bsm(spotPrice, strikePrice, daysToExp, riskFreeRate, vola)
print bsmVal
