from numpy import *
from scipy import *
import sys
sys.path.append("../src/")
import stochastic_oscillator

high  = array([34.7500, 34.7500, 34.2188, 33.8281, 33.4755, 33.4688, 34.3750, 34.7188, 34.6250,34.9219]);
low   = array([33.5312, 33.9062, 33.6875, 33.2500, 33.0000, 32.9375, 33.2500, 34.0469, 33.9375,34.0625]);
close = array([34.3125, 32.1250, 33.7500, 33.6406, 33.0156, 33.0469, 34.2969, 34.1406, 34.5469,34.3281]);

d_method = 'ema'
[per_k, per_d] = stochastic_oscillator.stoc_osc(high, low, close, 5,3,3, d_method)
