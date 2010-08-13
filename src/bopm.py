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

##
#
#  spotPrice     - current stock price
#  strikePrice   - strike price
#  volatility    - Volatility (unit is %)
#  daysToExp     - days to experiation.
#  riskFreeRate  - risk Free Rate of return
#
#
#  Notes
#  * Interest rate on a three-month U.S. Treasury bill is often used as 
#	 the risk-free rate
##
def bopm(spotPrice, strikePrice, volatility, daysToExp, riskFreeRate):
    # convert to a percentage
    v = volatility/100;
    # Period of each stage, for example, every stage will represent 2 days.
    T = 1;
    # based on log-normal distribution
    u = exp(sqrt(T/365.0) * v);
    # Recipocal of the up, such that a good follow by a bad, results in the original value
    d = 1/u;

    r = riskFreeRate* T/365.0;
    # compute probability of a up
    p = (1 + r - d) / (u - d);
    q = 1-p;
    
#    spotPrice =50;
#    strikePrice =50;

    Y = zeros(daysToExp);



    numStates = daysToExp;

    # Compute Final State
    nu = numStates -1;
    nd = 0
    for index in arange(0, numStates):
        Y[index] = max(spotPrice * u**nu * d**nd - strikePrice, 0);
        nu = nu - 1;
        nd = nd + 1;
        
    print(Y);
    # Traverse trellis to todays, to determine option price
    for numStates in arange(daysToExp - 1, 0, -1):
        Yn = zeros(daysToExp-1);
        for index in arange(0, numStates):
            Yn[index] = (p * Y[index] + q * Y[index+1]) / (1+r);
            print(Yn);
        Y = Yn;
    return Y[0]
