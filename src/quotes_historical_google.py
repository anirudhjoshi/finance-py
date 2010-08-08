##
#  Google Finance historical data feed.
#  Uses url request
#
#
## 

## Example Google url to get BP from Jun 5, 2008 to Jul 4, 2010
#http://www.google.com/finance/historical?q=bp&startdate=Jun+5+2008&enddate=Jul+4+2010&output=csv

# External libs
import httplib
import datetime
from scipy import *
from numpy import *
#def getData(symbol, exchange="", daysBack=365):
#    symbols    (mandatory)
#    exchange   (optional)
#    endDate    (1)
#    startDate  (1)
#    daysBack   (2)  
def getData(symbol, **kargs):#startDate, endDate,  ):
    
    if kargs.has_key("exchange"):
      exchange = kargs.get("exchange");
      if not exchange =="":
        exchange = exchange+":";
      
    else:
      exchange = "";
    
    
    if kargs.has_key("daysBack"):
      daysBack  = kargs.get("daysBack");
      startDate = datetime.date.today();
      endDate   = endDate - datetime.timedelta(daysBack);
    else:
      startDate = kargs.get("startDate");
      endDate   = kargs.get("endDate");
    




    conn = httplib.HTTPConnection("www.google.com")
 
  
    subUrl = "/finance/historical?q=%s%s&startdate=%s&enddate=%s&output=csv" % (symbol,exchange, startDate.strftime("%b+%d+%Y"),  endDate.strftime("%b+%d+%y"))

    conn.request("GET", subUrl)
    r1 = conn.getresponse()

    print r1.status, r1.reason

    data1 = r1.read()
 
    data1 = data1.split('\n')
    N =size(data1)

    if __debug__ :
        print "www.google.com"+ subUrl
    
    vDate  = zeros((N-2))
    vOpen  = zeros((N-2))
    vHigh  = zeros((N-2))
    vLow   = zeros((N-2))
    vClose = zeros((N-2))
    vVolume= zeros((N-2))
    # ignore first row, since it is a header and last row since it only contains a ']'
    for index in range(1,N-1):
        row = data1[index].split(',');
        print row

        # convert to date time, and the convert to ordinal time. 
        g = datetime.datetime.strptime(row[0], "%d-%b-%y")
        vDate[index - 1] = datetime.datetime.toordinal(g);
        vOpen[index - 1] = row[1]
        vHigh[index - 1] = row[2]
        vLow[index - 1] = row[3]
        vClose[index - 1] = row[4]
        vVolume[index - 1] = row[5]
    return vDate, vOpen, vHigh, vLow, vClose, vVolume
