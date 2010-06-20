################################################################################
# Author - Ray Salem
# Description
# Creation date
# History
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
################################################################################
from numpy import *
from scipy import *


# Period of each stage, for example, every stage will represent 2 days.
T = 1;
volatility =  30 / 100.0;
# based on log-normal distribution
u = exp(sqrt(T/365.0) * volatility);
# Recipocal of the up, such that a good follow by a bad, results in the original value
d = 1/u;
r = 0.1 * T/365.0;
# compute probability of a up
p = (1 + r - d) / (u - d);
q = 1-p;

spotPrice =50;
strikePrice =50;

periods = 3;
Y = zeros(periods);



numStates = periods;

# Compute Final State
nu = numStates -1;
nd = 0
for index in arange(0, numStates):
    Y[index] = max(spotPrice * u**nu * d**nd - strikePrice, 0);
    nu = nu - 1;
    nd = nd + 1;

print(Y);

for numStates in arange(periods - 1, 0, -1):
    Yn = zeros(periods-1);
    for index in arange(0, numStates):
        Yn[index] = (p * Y[index] + q * Y[index+1]) / (1+r);
    print(Yn);
    Y = Yn;

