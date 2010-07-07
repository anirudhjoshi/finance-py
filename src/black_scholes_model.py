################################################################################
# Author - Ray Salem
# Description - Computes the value of an option based on black scholes model
# Creation date
# History
# References
#			- Options as a strategic investment
#                       - http://www.quickmba.com/finance/black-scholes/
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
#	return 1 - stats.erfc(x)
    # save the sign of x
    sign = 1
    if x < 0: 
        sign = -1
    x = abs(x)

    # constants
    a1 =  0.254829592
    a2 = -0.284496736
    a3 =  1.421413741
    a4 = -1.453152027
    a5 =  1.061405429
    p  =  0.3275911

    # A&S formula 7.1.26
    t = 1.0/(1.0 + p*x)
    y = 1.0 - (((((a5*t + a4)*t) + a3)*t + a2)*t + a1)*t*math.exp(-x*x)
    return sign*y # erf(-x) = -erf(x)

# Stock price
p = 133.83;

# Strike price
s = 135;

# Time remaining to expiration (unit is days)
t = 9;

# Current Risk free interest rate. (unit is percentage) 
r = 1;

#Volatility measured by annual standard deviation (unit is percentage)
v = 39.79;


# normalize
r = r/100.0;
v = v/100.0;
t = t/365.0;
d1 = (log(p/s) + ( r + v**2 / 2.0 ) *t) / (v * sqrt(t));
d2 = d1- v * sqrt(t);


# The function is the CDF for a stand normal distribution u=0, sigma = 1.
N1 = 1/2 * (1 + erf(d1/sqrt(2)));
N2 = 1/2 * (1 + erf(d2/sqrt(2)));
callPrice = p * N1 - s * exp(-r * t) * N2;
putPrice  = callPrice - p + s * exp(-r*t)

print callPrice
print putPrice
