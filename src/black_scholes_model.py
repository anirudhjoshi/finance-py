################################################################################
# Author - Ray Salem
# Description - Computes the value of an option based on black scholes model
# Creation date
# History
# References
#			- Options as a strategic investment
# Notes
#			- ln is the normal logarithm
#			- N(x) is the CDF of the a stnard normal distribution. 
#			- In practice, however, the risk-free rate does not exist because even 
#			    the safest investments carry a very small amount of risk. Thus, the
#				interest rate on a three-month U.S. Treasury bill is often used as 
#				the risk-free rate. 
################################################################################

# Will use treat division operands as rational numbers rather then integer. 
from __future__ import division

from numpy import *
from scipy import *

def erf(x):
	return 1 - stats.erfc(x)

# Stock price
p = 45;

# Strike price
s = 50;

# Time remaining to expiration (unit is days)
t = 60;

# Current Risk free interest rate. (unit is percentage) 
r = 10;

#Volatility measured by annual standard deviation (unit is percentage)
v = 30;


# normalize
r = r/100.0;
v = v/100.0;
t = t/365.0;
d1 = (log(p/s) + ( r + v**2 / 2.0 ) *t) / (v * sqrt(t));
d2 = d1- v * sqrt(t);


# The function is the CDF for a stand normal distribution u=0, sigma = 1.
N1 = 1/2 * (1 + erf(d1/sqrt(2)));
N2 = 1/2 * (1 + erf(d2/sqrt(2)));
price = p * N1 - s * exp(-r * t) * N2;


