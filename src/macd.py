################################################################################
# Copyright (C)  2010 Ray M. Salem
# http://code.google.com/p/finance-py/
# Distributed under the GPL license Version 3.0 ( See accompanying file 
# License_ or copy at http://code.google.com/p/finance-py/LICENSE)
################################################################################

# Creator Ray Salem
from numpy import *
from scipy import *
import moving_average
#
# fastLength - represent fast changing ema (small vale)
# slowLength - represent slow changing ema (large value)

# Return
# macdOut    - different between fast and slow ema
# signal     - ema of macdOut
# divergence - macdOut - signal
def macd(input, fastLength, slowLength, signalLength):
    N = input.__len__();

    emaFast = zeros((N))
    emaSlow = zeros((N))
    signal  = zeros((N))

    # Slow EMA
    emaSlow = moving_average.ema(input, slowLength);
    # Fast EMA
    emaFast = moving_average.ema(input, fastLength);
    # Take the difference of the two
    macdOut = emaFast - emaSlow
    signal = moving_average.ema(macdOut, signalLength);
    divergence = macdOut - signal;
    return [macdOut,signal,divergence]
