################################################################################
# Author - Ray Salem
# Description -Computes volatility of a stock.
# Creation date
# History
#
#
#
# References
#            http://www.riskglossary.com/link/volatility.htm
#            http://en.wikipedia.org/wiki/Volatility_(finance)
# Online calculator
#            http://www.optionistics.com/f/strategy_calculator

from numpy import *

## include source path
import sys
sys.path.append("../src/")

##
# Computes the volatility over the range 
#   Compute as the std ( Log (current / prev) ) * sqrt( Length) * 100
#
#
def volatility(spotPrices):
    deltaLn = log(spotPrices[1:] /spotPrices[:-1] )    
    sigma   = std(deltaLn);
    N       = size(spotPrices)
    sigmaN  = sigma * sqrt(N)
    return sigmaN * 100;
