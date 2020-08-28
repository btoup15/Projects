##############################
#   Author: Benjamin Toups
#       8/28/2020
#        For Mel
##############################

import os
import datetime
import csv
path = 'C:/Users/ben/Desktop/General/Documents/'
outfile = 'C:/Users/ben/Desktop/metadata.csv'

#List of all files in the specified directory
files = os.listdir(path)

#Writes header row to the CSV (optional)
with open(outfile, 'a') as fp:
    headers = ['File Name', 'File Type', 'Date Modified']
    wr = csv.writer(fp, dialect = 'excel', lineterminator = '\n')
    wr.writerow(headers)

#Class for a file in the specified directory with properties name, file type, and date modified
class infile:
    def __init__(self, name, ftype, date):
        self.name = name
        self.ftype = ftype
        self.date = date

    def printData(self):
        '''prints file properties in a readable format'''
        print('File name: {}, File Type: {}, Date Modified: {}'.format(self.name, self.ftype, self.date))

    def printToCSV(self, csvfile):
        '''writes file properties to a given csv'''
        data = [self.name, self.ftype, self.date]
        with open(csvfile, 'a') as fp:         
            wr = csv.writer(fp, dialect='excel', lineterminator = '\n')
            wr.writerow(data)

#Empty list that will be populated with a file object for each file in the specified directory
fileobjs = []

#Populating the file object list
for i in files:
    fileobjs.append(infile(name = os.path.splitext(i)[0], ftype = os.path.splitext(i)[1], 
    date = datetime.datetime.fromtimestamp(os.stat(path+i).st_mtime).strftime('%Y-%m-%d-%H:%M')))

#Calling the printToCSV method for each object in the list
for i in fileobjs:
    i.printToCSV(outfile)

