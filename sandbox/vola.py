## include source path
import sys
sys.path.append("../src/")

from historical_data_obj import * 
from volatility import * 
import matplotlib.pyplot as plt

data = HistoricalDataObj()
data.initialize("bp",365);

print volatility(data.vClose)


#  current minus the   previous
delta  = data.vClose[1:] - data.vClose[:-1] ;
deltaP = delta / data.vClose[1:] * 100;
deltaLn = log(data.vClose[1:] /data.vClose[:-1] );
v = std(deltaLn) ;
#there are 252 trading days in any given year
v2 = v / sqrt(1.0/252.0);
print(v)  * 100
print(v2) * 100



plt.hist(deltaLn * 100)
plt.show()
