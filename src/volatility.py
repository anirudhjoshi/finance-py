################################################################################
# Copyright (C)  2010 Ray M. Salem
# http://code.google.com/p/finance-py/
# Distributed under the GPL license Version 3.0 ( See accompanying file 
# License_ or copy at http://code.google.com/p/finance-py/LICENSE)
################################################################################

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
# spotPrices - spot price
# scale factor 
#
def volatility(spotPrices, scaleFactor = -1):
    deltaLn = log(spotPrices[1:] /spotPrices[:-1] )    
    sigma   = std(deltaLn);
    N       = size(spotPrices)
    if(scaleFactor == -1):
        sigmaN = sigma * sqrt(N)
    else:
        sigmaN = sigma * sqrt(scaleFactor)
    return sigmaN * 100;
