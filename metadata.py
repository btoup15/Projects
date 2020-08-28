import os
import glob
import datetime
import csv
path = 'C:/Users/ben/Desktop/General/Documents/'
outfile = 'C:/Users/ben/Desktop/metadata.csv'

files = os.listdir(path)

with open(outfile, 'a') as fp:
    headers = ['File Name', 'File Type', 'Date Modified']
    wr = csv.writer(fp, dialect = 'excel', lineterminator = '\n')
    wr.writerow(headers)


class infile:
    def __init__(self, name, ftype, date):
        self.name = name
        self.ftype = ftype
        self.date = date

    def printData(self):
        print('File name: {}, File Type: {}, Date Modified: {}'.format(self.name, self.ftype, self.date))

    def printToCSV(self, csvfile):
        data = [self.name, self.ftype, self.date]
        with open(csvfile, 'a') as fp:         
            wr = csv.writer(fp, dialect='excel', lineterminator = '\n')
            wr.writerow(data)

fileobjs = []

for i in files:
    fileobjs.append(infile(name = os.path.splitext(i)[0], ftype = os.path.splitext(i)[1], 
    date = datetime.datetime.fromtimestamp(os.stat(path+i).st_mtime).strftime('%Y-%m-%d-%H:%M')))

for i in fileobjs:
    i.printToCSV(outfile)

