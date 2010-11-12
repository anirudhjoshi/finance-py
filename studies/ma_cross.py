################################################################################
# Copyright (C)  2010 Ray M. Salem
# http://code.google.com/p/finance-py/
# Distributed under the GPL license Version 3.0 ( See accompanying file 
# License_ or copy at http://code.google.com/p/finance-py/LICENSE)
################################################################################

##
# Moving average cross, positively and negatively
# Expects historical data.
#

from numpy import *
from scipy import *

import moving_average

def maCross(data, length):
    ma = moving_average.ma(data.vClose, length)
    N = size(data.vClose);
    # days going back
    M = 25;
    for index in arange(N-M, N):
        # find the last index associated with a value below the moving average
        if(ma[index-1] > data.vClose[index]):
            minIndex = index;
    for index in arange(minIndex, N):
        if(ma[minIndex] < data.vClose[index]):
            maxIndex = index;
            break

    print maxIndex;
    print data.vClose[maxIndex]
    
