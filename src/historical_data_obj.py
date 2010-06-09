################################################################################
#				Copyright (c) 2009 Omni Wireless Communication Inc
#	   All rights are reserved. Reproduction in whole or in parts is
#	   prohibited without the written consent of the copyright owner.
#
#			   Address:  3755 avocado Blvd
#						 Suite 434
#						 La Mesa, Ca, 91941
#
#			   Tel:	619-378-6000
#			   Web:	www.omniwcomm.net
#
################################################################################
from numpy import *
from scipy import *

import moving_average
from matplotlib.finance import quotes_historical_yahoo
import sys
from datetime import date,timedelta

import matplotlib.pyplot as plt


##############################################################################
## Historical Data Object
#   STored in vectors where every element represents a single date
#
#
#
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
        ## Vectror of dates
        self.vDates     = array([])
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
        ## Number of entries (length of vector)
        self.N          = 0;
        ## Quotes raw data created by data feed.
        self.quotes     = [];
    ##############################################################################
    ## Initialization routine
    # @param symbol symbol of historical data to be retrieved
    # @param data1 start date
    # @param date2 end date
    # @param interval period of samples, must be an integer and greater then 1, for example
    #   2, would return samples for every other day.
    # @param resolition, is allways 1
    # @param dataFeedType - data feed up, currently onlys supporting yahoo.
    def initialize( self,stockTicker, date1, date2, interval = 1, resolution = 1, dataFeedType = "yahoo"):

        self.stockTicker = stockTicker;
        if(dataFeedType =="yahoo"):
            self.quotes = quotes_historical_yahoo(self.stockTicker, date1, date2)

        self.N          = self.quotes.__len__();
        self.vDates     = zeros(self.N)
        self.vOpen      = zeros(self.N)
        self.vClose     = zeros(self.N)
        self.vHigh      = zeros(self.N)
        self.vLow       = zeros(self.N)
        self.vVolume    = zeros(self.N)



        index = 0;
        for lines in self.quotes:
            self.vDates[index]  = lines [0];
            self.vOpen[index]   = lines [1];
            self.vClose[index]  = lines [2];
            self.vHigh[index]   = lines [3];
            self.vLow[index]    = lines [4];
            self.vVolume[index] = lines [5];
            index =  index +1;