#!/usr/bin/env python

# +-+-+-+-+-+-+ +-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+
# PERFORMANCE FILE READER
# +-+-+-+-+-+-+ +-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+

import sys
import os
from datetime import datetime, timedelta
import math
#import termplot as tp
#from terminalplot import plot,get_terminal_size
#import gnuplotlib as gp
import matplotlib.pyplot as plt
import numpy as np

# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
ERROR_READING_FILE = 'File not exist or is not accessible by permissions'

# +-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+
# CLASS DEFINITION
# +-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+

class OsAgent:

    FORMAT_STRING = "%Y-%m-%d %H:%M:%S"
    syslen = 0
    myFile = ""
    myValueList = []
    finalValueList = []
    hoursList = []
    mediaList = []
    xList = []
    yList = []

    @staticmethod
    def clearScreen():
        os.system('clear')

    @staticmethod
    def elegantExit():
        sys.exit()

    @staticmethod
    def waitPlease(mySeconds):
        time.sleep(mySeconds)

    @staticmethod
    def myFileExist(myfile):
        if os.path.exists(myfile):
            return True
        else:
            return False

    def countSysParameter(self):
        self.syslen = len( sys.argv )

    def printSysParameters(self):
        if self.syslen > 1:
            #for indiceparameter in enumerate(sys.argv):
            self.myFile = sys.argv[1]
            tempString = "Evaluating file: %s" % ( self.myFile )
            print tempString
        else:
            print "No file provided!"

    def openMyFile(self):
        with open(self.myFile,'r') as myLog:
            for myLine, myDataLine in enumerate(myLog):
                myFields = myDataLine.split(';')
                if myLine > 0:
                    myDateString = myFields[0] + " " + myFields[1]
                    myDatedate = datetime.strptime(myDateString,self.FORMAT_STRING)
                    myFloatValue = float(myFields[12])
                    myTempTuple = (myDatedate, myFloatValue)
                    self.myValueList.append(myTempTuple)

    def processAverages(self):
        for myDatedate,myValueRaw in self.myValueList:
            print myValueRaw
            if self.finalValueList:
                # - Get the hours list
                for myHours in self.finalValueList:
                    self.hoursList.append(myHours[0])
                if int(myDatedate.hour) in self.hoursList:
                    for removeIndex, myData in enumerate(self.finalValueList):
                        myHour, myValue, myCount = myData
                        if int(myDatedate.hour) == int(myHour):
                            myTripletOld = self.finalValueList.pop(removeIndex)
                    valueHour, valueData, valueCount = myTripletOld
                    finalValue = valueData + myValueRaw
                    valueCount += 1
                    myTriplet = (int(myDatedate.hour), finalValue, valueCount)
                    print myTriplet
                    self.finalValueList.append(myTriplet)
                else:
                    myTriplet = (int(myDatedate.hour),myValueRaw,1)
                    print myTriplet
                    self.finalValueList.append(myTriplet)
            else:
                myTriplet = (int(myDatedate.hour),myValueRaw,1)
                print myTriplet
                self.finalValueList.append(myTriplet)
        # - Average Calculation
        for myData in self.finalValueList:
            horaFinal, dataFinal, quantities = myData
            laMediaAritmeticaEsIgualA = float(dataFinal)/float(quantities)
            finalTuple = (horaFinal,laMediaAritmeticaEsIgualA)
            self.mediaList.append(finalTuple)

        print self.finalValueList
        print self.mediaList

    def printTrend(self):
        # - Termfinalplot routine
        #get_terminal_size()
        for plotData in  self.mediaList:
            x, y = plotData
            self.xList.append(x)
            self.yList.append(y)
        #plot(self.xList,self.yList)
        npX = np.asarray(self.xList, dtype=np.int)
        npY = np.asarray(self.yList, dtype=np.float32)
        plt.plot(npX,npY)
        plt.title('Performance Log')
        plt.xlabel('Hour')
        plt.ylabel('Average EPS')
        for myX,myY in zip( self.xList,self.yList):
            plt.text(myX,myY, str(round(myY,2)))
        plt.show()

# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

osbox = OsAgent()
osbox.countSysParameter()
osbox.printSysParameters()
if OsAgent.myFileExist(osbox.myFile):
    osbox.openMyFile()
    #print(osbox.myValueList)
    osbox.processAverages()
    osbox.printTrend()
else:
    print(ERROR_READING_FILE)
