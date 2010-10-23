
from numpy import *
from scipy import *
# Eponential Moving average
# in - input, out-output, length
def ema(input,length):
    N = input.__len__();
    output = zeros(N);
    output[0] = input[0];
    sum = input[0];
    
    sf1 = 2.0/ (length+1.0);
    sf2 = 1.0-sf1;
    indxO = 1;
    for indxI in arange(1,N):
        sum = input[indxI] *sf1 + sum * sf2;
        output[indxO] = sum;
        indxO = indxO +1;
    return output

# moving avergage
def ma(input, length):
    weights = ones(length) / length
    output = convolve(input, weights, mode='full')[:len(input)]
    return output;
# Moving average
def sma(input, length):
    return ma(input, length)
