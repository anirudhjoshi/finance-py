################################################################################
# Copyright (C)  2010 Ray M. Salem
# http://code.google.com/p/finance-py/
# Distributed under the GPL license Version 3.0 ( See accompanying file 
# License_ or copy at http://code.google.com/p/finance-py/LICENSE)
################################################################################


################################################################################
# Will read option data from yahoo, and will output files contain the appropiate 
# data.
# Future version will improve interface and error handling
################################################################################
from numpy import *
import urllib
import re
import csv

readFile            = 0;
readSymbolFile      = 0;
#   "sp500" - list of S%P 500 component stocks
#   "dia" - list of Dow Jones component stocks
#   "index" - list of index stocks: SPY DIA QQQ
#   "user"  - user defined list of stocks
readSymbolFileName  = "sp500"

securityA   = ["qcom"]
date        = "2011-02";
verbose_    = 2
################################################################################
# security - Security Name, i.e. QQQQ
# date - format is "YEAR-MONTH_NUM", where month_num, is the numerical representation
# of the month for example 2007-11
def readYahooStockOptions(security, date, verbose = 1):
    if(readFile):
        fid = open("C:\\work\\\\option_data_"+security+".html",'r');
        fileString =fid.readlines();
        s = fileString.__str__();
    else:
        # Get a file-like object for the yahoo option web page
        url = "http://finance.yahoo.com/q/os?s="+security+"&m=" + date
        if(verbose >1):
            print url
        f = urllib.urlopen(url)
        # Read from the object, storing the page's contents in 's'.
        s = f.read()
        f.close()
    if(verbose > 2):
        print s

    # check if this string is present, if so, then we didnt find the symbol
    optionDataValid = 1;
    if(s.find("Get Quotes Results for") != -1):
        optionDataValid = 0;
        [price,priceChange,priceChangePer] = [0,0,0]
        strData = s;
    else:
        fid = open("c:\\work\\bin\\option_data_"+security+".html",'w')
        fid.writelines(s)
        fid.close()

        [price,priceChange,priceChangePer] = parsePriceData(s,verbose)
        #(1) Parse out all data before the table
        exps    = "Friday,(.*)";
        reOut   = re.search(exps, s);

        if(reOut == None):
            optionDataValid = 0;
            strData = s;
        else:
            strData = reOut.group(0).__str__();
    return [strData,optionDataValid, price,priceChange,priceChangePer]
################################################################################
#
# return
#    current market price
#    price change from last closing
#    price change (%)
def parsePriceData(fileString, verbose = 1.0):
    exps = "<big>.*?\">([0-9.,]*?)<.*?;\">([0-9.]*?)<.*?;\">.*?([0-9.]*?)%"
    reOut = re.search(exps, fileString)
    price = float(reOut.group(1).replace(',',''))
    priceChange = float(reOut.group(2))
    priceChangePer = float(reOut.group(3))
    if(verbose > 1):
        print price
    return [price,priceChange,priceChangePer]
################################################################################
# return
#
#
#
#  numPoints - number of different strike prices.
def parseOptionData(strData, verbose = 1):
    #(1) Parse out all data before the table
    #exps    = "Fri,(.*)";
    #reOut   = re.search(exps, fileString);
    #strData = reOut.group(0);

    # (2) Seperate string into indivual lines for each strike price calls/puts
    strSplit = strData.split("href")

    # (3) Parse each line on at a time
    exps = "q\?s=(.*?)\".*?>([0-9]{1,3}\.[0-9]{2})<.*?>([0-9]{1,3}\.[0-9]{2})<.*?>([0-9]{1,3}\.[0-9]{2})<.*?>([0-9]{1,3}\.[0-9]{2})<.*?>([0-9,]{1,6})<.*?>([0-9,]{1,6})<"
    # get the strike price
    exps2 = ".*?([0-9]{1,3}\.[0-9]{2})"
    index = 0;
    securityA =[]
    strikePrice = zeros(500)
    callProcess = 1
    # Create an empty array
    callData = zeros((500,6))
    putData  = zeros((500,6))
    for str in strSplit:
        # replace N/A with a 0.01 (very small value)
        str = str.replace("N/A","0.01")
        reOut       = re.search(exps, str);
        if(reOut != None):
            if(verbose > 3):
                print str                            
            security    = reOut.group(1);
            mkPrice     = float(reOut.group(2));# convert string to float
            change      = float(reOut.group(3));
            bid         = float(reOut.group(4));
            ask         = float(reOut.group(5));
            volume      = float(reOut.group(6).replace(",","")) # remove commas
            openInt     = float(reOut.group(7).replace(",",""))
            values      = array([mkPrice, change, bid, ask, volume, openInt])
            if(1):
              print reOut.group(6)           
            jj = 0;
            if(callProcess == 1):
                for dat in values:
                    callData[index,jj] = dat;
                    jj = jj + 1;
                callProcess = 0
            else:
                for dat in values:
                    putData[index,jj]  = dat;
                    jj = jj + 1;
                callProcess = 1
                index = index + 1

            securityA.append(security)
        else:
            reOut       = re.search(exps2, str);
            if(reOut != None):
                if(verbose > 2):
                    print str
                strikePrice[index]     = float(reOut.group(1));
    numPoints = index;
    # remove the zeros
    callDataA    = callData[0:numPoints];
    putDataA     = putData[0:numPoints];
    strikePriceA = strikePrice[0:numPoints];    
    return [callDataA,putDataA,strikePriceA,securityA, numPoints]
################################################################################
# main loop
################################################################################
#get list of securities
print "started Exp Data (" + date +")"
if(readSymbolFile ==1):
    reader = csv.reader(open("C:\\work\\"+readSymbolFileName+".csv", "rb"))
    securityA = []
    for row in reader:
        securityA.append(row[0])
for security in securityA:
    #remove spaces
    security = security.replace(" ","")
    [fileString,optionDataValid,buyPrice,priceChange,priceChangePer] = readYahooStockOptions(security, date,verbose_);
    fileString = fileString.__str__();

    if(optionDataValid == 1):
        #[buyPrice,priceChange,priceChangePer] = parsePriceData(fileString);
        [callData,putData, strikePrice,optionNames,numPoints] = parseOptionData(fileString)

        # Write Market Data, to security.csv
        fidData = open("C:\\work\\bin\\"+security+".txt",'w');
        fidData.writelines(buyPrice.__str__() + "\n" + priceChange.__str__() + "\n" + priceChangePer.__str__() +"\n"+numPoints.__str__());
        fidData.close()

        fidCallData     = open("C:\\work\\bin\\"+security+".call.txt",'w');
        fidPutData      = open("C:\\work\\bin\\"+security+".put.txt",'w');
        fidStrikePrice  = open("C:\\work\\bin\\"+security+".strike_price.txt",'w');
        fidAll          = open("C:\\work\\bin\\"+security+".txt",'w');
        # write call data,to security.call.csv

        secNameIndex = 0;
        NcharSecName = len(security);
        for index in range(0,numPoints):
            fidAll.writelines(optionNames[index*2 + 0] + "\t")
            for data  in callData[index]:
                fidCallData.writelines(data.__str__() + "\t")
                fidAll.writelines(data.__str__() + "\t")            
            fidCallData.writelines("\n");
            fidAll.writelines(strikePrice[index].__str__() + "\n")

            fidAll.writelines(optionNames[index*2 + 1] + "\t")
            for data  in putData[index]:
                fidPutData.writelines(data.__str__() + "\t")
                fidAll.writelines(data.__str__() + "\t")
            fidPutData.writelines("\n");
            fidAll.writelines(strikePrice[index].__str__() + "\n")
            

            fidStrikePrice.writelines(strikePrice[index].__str__() + "\n")

            secNameIndex = secNameIndex + 2;

        fidCallData.close()
        fidPutData.close()
        fidStrikePrice.close();
        fidAll.close()
print "done"
