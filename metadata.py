import os
import glob
import datetime
path = 'C:/Users/ben/Desktop/General/Documents/misc/'


files = os.listdir(path)


class file:
    def __init__(self, name, ftype, date):
        self.name = name
        self.ftype = ftype
        self.date = date
    def printdata(self):
        print('File name: {}, File Type: {}, Date Modified: {}'.format(self.name, self.ftype, self.date))

#mtime = os.stat(path + files[1]).st_mtime
#timestamp = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d-%H:%M')
#print(timestamp)

fileobjs = []

for i in range(len(files)):
    fileobjs.append(file(name = os.path.splitext(files[i])[0], ftype = os.path.splitext(files[i])[1], 
    date = datetime.datetime.fromtimestamp(os.stat(path+files[i]).st_mtime).strftime('%Y-%m-%d-%H:%M')))

for i in fileobjs:
    i.printdata()

