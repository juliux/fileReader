#!/usr/bin/env python

# +-+-+-+-+-+-+ +-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+
# PERFORMANCE FILE READER
# +-+-+-+-+-+-+ +-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+

import sys
import os
from datetime import datetime, timedelta
import math
import csv

# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
ERROR_READING_FILE = 'File not exist or is not accessible by permissions'

# +-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+
# CLASS DEFINITION
# +-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+

class OsAgent:

    FORMAT_STRING = "%Y-%m-%dT%H:%M"
    FORMAT_STRING2 = "%Y%m%d-%H%M"
    WAIT_REPORT_NAME = "wait-report"
    syslen = 0
    myFile = ""
    myValueList = []
    finalValueList = []
    hoursList = []
    mediaList = []
    xList = []
    yList = []
    myFinalFileName =""

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
                myDateString = myFields[1]
                myTask = myFields[2]
                myFTPS = float(myFields[7])
                myDatedate = datetime.strptime(myDateString,self.FORMAT_STRING)
                myFmean = float(myFields[6])
                myMeanN = int(myFields[8])
                myTempTuple = (myDatedate,myTask,myFmean,myMeanN,myFTPS)
                #print myTempTuple
                self.myValueList.append(myTempTuple)

    def printToCSV(self):
        self.myFinalFileName = self.WAIT_REPORT_NAME + "." + datetime.strftime(self.myValueList[0][0],self.FORMAT_STRING2) + "." + self.myFile
        print self.myFinalFileName
        with open(self.myFinalFileName,'wb') as out:
            csv_out=csv.writer(out)
            #csv_out.writerow(['name','num'])
            csv_out.writerows(self.myValueList)

# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

osbox = OsAgent()
osbox.countSysParameter()
osbox.printSysParameters()
if OsAgent.myFileExist(osbox.myFile):
    osbox.openMyFile()
    osbox.printToCSV()
    #print(osbox.myValueList)
    #osbox.processAverages()
    #osbox.printTrend()
else:
    print(ERROR_READING_FILE)
