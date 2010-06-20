
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