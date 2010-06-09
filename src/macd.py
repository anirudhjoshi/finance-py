################################################################################
#                Copyright (c) 2009 Omni Wireless Communication Inc
#       All rights are reserved. Reproduction in whole or in parts is
#       prohibited without the written consent of the copyright owner.
#
#               Address:  3755 avocado Blvd
#                         Suite 434
#                         La Mesa, Ca, 91941
#
#               Tel:    619-378-6000
#               Web:    www.omniwcomm.net
#
################################################################################
from numpy import *
from scipy import *
import moving_average
def macd(input, slowLength, fastLength, signalLength):
    N = input.__len__();

    ema1out = zeros((N))
    ema2out = zeros((N))
    ema     = zeros((N))

    # 1st EMA
    moving_average.ema(input, ema1out, fastLength);
    # 2nd EMA
    moving_average.ema(input, ema2out, slowLength);
    # Take the difference of the two
    macdOut = ema1out - ema2out
    moving_average.ema(macdOut, ema, signalLength);
    divergence =macdOut -ema;
    return [macdOut,ema,divergence]