################################################################################
# Copyright (C)  2010 Ray M. Salem
# http://code.google.com/p/finance-py/
# Distributed under the GPL license Version 3.0 ( See accompanying file 
# License_ or copy at http://code.google.com/p/finance-py/LICENSE)
################################################################################

# Stochastic Oscillator.py
#
#
#  History
#  Date     - Author    - Description
#---------------------------------------
#  10/16/10 - Ray Salem - Creation
#
#
#  High  - Vector of highs, where each element is for one period
#  low   - '
#  close - '

#  d_method - 'sma'--> simple moving average, 'ema'--> exponential moving average

from numpy import *
from scipy import *
import moving_average
def stoc_osc(high, low, close, k_periods, k_slow_periods, d_periods, d_method):
    N = close.__len__();
    per_k = per_d = zeros(N);
    numerator = zeros(N);
    denominator  = zeros(N);
    for index in arange(0,k_periods-1):
        max_high    = max(high[0:index+1]);
        min_low     = min(low[0:index+1]);
        numerator[index]   = abs(close[index] - min_low);
        denominator[index] = abs(max_high - min_low); # abs to handle negative values
        
    for index in arange(k_periods-1,N):
        max_high    = max(high[index-k_periods+1:index+1]);
        min_low     = min(low[index-k_periods+1:index+1]);
        numerator[index]   = close[index] - min_low;
        denominator[index] = max_high - min_low;
        
    # %K Slowing periods, sum over last slowing periods (moving average work since we are doing a division)
    num = moving_average.sma(numerator, k_slow_periods);
    den = moving_average.sma(denominator, k_slow_periods);
    for index in arange(0, N):
        if(den[index] == 0):
            per_k[index] = 100;
        else:
            per_k[index] = num[index] / den[index] * 100;

    if(d_method == "ema"):
        per_d = moving_average.ema(per_k, d_periods);
    elif(d_method == "sma"):
        per_d = moving_average.ema(per_k, d_periods);
    else:
        print("incorrect moving average method specified,( " + d_method + " ) is not supporteD");
    return [per_k, per_d];
