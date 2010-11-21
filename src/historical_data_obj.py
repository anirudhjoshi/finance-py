################################################################################
# Copyright (C)  2010 Ray M. Salem
# http://code.google.com/p/finance-py/
# Distributed under the GPL license Version 3.0 ( See accompanying file 
# License_ or copy at http://code.google.com/p/finance-py/LICENSE)
################################################################################

from numpy import *
from scipy import *

from matplotlib.finance import quotes_historical_yahoo
from datetime import date, timedelta

import quotes_historical_google
import sys


##############################################################################
## Historical Data Object
#   STored in vectors where every element represents a single date
#
#
# Note;
#  index 0 is the earliest date, and Index is the lates date (ie. 0-->10/1/10 1-->10/2/10)
# Todo:
# Google date feed needs more support for date range, date values
#
import datetime
class HistoricalDataObj:
    """Historical Finance Data Object"""
    #Fields
    vOpen  = array([])
    vClose = array([])
    stockTicker = ""

    ##############################################################################
    ## Constructor
    def __init__(self):
        ## Stock ticker (symbol)
        self.stockTicker= ""
        ## Vectror of dates dah format
        self.vDateInt   = array([])
        self.vDate      = array([])
        ## vector of open values
        self.vOpen      = array([])
        ## Vector closes
        self.vClose     = array([])
        ## Vector of days highs
        self.vHigh      = array([])
        ## Vector of lows
        self.vLow       = array([])
        ## Vector of volume
        self.vVolume    = array([])
        ## Vector of log(price change)
        self.vLdata     = array([])
        ## Number of entries (length of vector)
        self.N          = 0;
        ## Quotes raw data created by data feed.
        self.quotes     = [];
    ## Same as above but the range is from today to days back
    def initialize( self, stockTicker, daysBack, interval = 1, resolution = 1, dataFeedType = "yahoo", dateFormat="raw"):  
        # start data
        date1 = date.today() - timedelta(days=daysBack)
        # end
        date2 = date.today()
        self.initialize1(stockTicker, date1, date2, interval, resolution, dataFeedType)
    ##
    # Init attributes not set during initialiation 
    # type:
    #   "logData" - will set vLdata, as the log of the price change
    #
    def init(self,initType):
      if(initType =="logData"):
        self.vLdata   = zeros(self.N)
        vLdata        = log(self.vClose[1:] /self.vClose[:-1] )
                            
    ##############################################################################
    ## Initialization routine
    # @param symbol symbol of historical data to be retrieved
    # @param data1 start date
    # @param date2 end date
    # @param interval period of samples, must be an integer and greater then 1, for example
    #   2, would return samples for every other day.
    # @param resolition, is allways 1
    # @param dataFeedType - data feed up, currently onlys supporting yahoo.
    def initialize1( self,stockTicker, date1, date2, interval, resolution, dataFeedType):

        self.stockTicker = stockTicker;
        if(dataFeedType =="yahoo"):
            self.quotes = quotes_historical_yahoo(self.stockTicker, date1, date2)
            self.N          = self.quotes.__len__();
            self.vDateInt   = zeros(self.N)
            self.vDate      = empty(self.N, dtype=object);
            self.vOpen      = zeros(self.N)
            self.vClose     = zeros(self.N)
            self.vHigh      = zeros(self.N)
            self.vLow       = zeros(self.N)
            self.vVolume    = zeros(self.N)

            index = 0;
            for line in self.quotes:
                self.vDateInt[index]= line [0];
                self.vDate[index]   = date.fromordinal( int( line [0] ) )
                self.vOpen[index]   = line [1];
                self.vClose[index]  = line [2];
                self.vHigh[index]   = line [3];
                self.vLow[index]    = line [4];
                self.vVolume[index] = line [5];
                index =  index +1;
        elif (dataFeedType == "google"):
            self.vDateInt, self.vOpen, self.vHigh, self.vLow, self.vClose, self.vVolume = quotes_historical_google.getData(symbol=self.stockTicker, startDate=date1, endDate=date2);
            self.N = size(self.vDateInt);
            self.vDate      = empty(self.N, dtype=object);
            index = 0;
            for d in self.vDateInt:
                self.vDate[index] = date.fromordinal( int( d) );
                index = index + 1;
    
