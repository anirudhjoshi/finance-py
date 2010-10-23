
from numpy import *
from scipy import *
import moving_average
def macd(input, slowLength, fastLength, signalLength):
    N = input.__len__();

    ema1out = zeros((N))
    ema2out = zeros((N))
    ema     = zeros((N))

    # 1st EMA
    ema1out = moving_average.ema(input, fastLength);
    # 2nd EMA
    ema2out = moving_average.ema(input, slowLength);
    # Take the difference of the two
    macdOut = ema2out - ema1out
    ema = moving_average.ema(macdOut, signalLength);
    divergence =macdOut -ema;
    return [macdOut,ema,divergence]
