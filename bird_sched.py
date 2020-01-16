#####################
#  Author: Ben Toups
#   1/16/2020
#####################
import random
import csv

#number of birds apart of the experiment
birds = 24

#for each bird, creates a 3 week long list with 3 objects and 2 controls each week
for i in range(birds):
    w1 = []
    w2 = []
    w3 = []
    weeks = [w1,w2,w3]
    obj = [2,3,4,5,6,7,8,9,10]
    for i in weeks:
        t = 0
        while t < 3:
            i.append(obj.pop(random.randint(0,len(obj)-1)))
            t += 1
        i.extend([1,11])
        random.shuffle(i)
    sched = w1 + w2 + w3
    with open("C:/Users/ben/Desktop/birds.csv", "a") as fp:
        wr = csv.writer(fp, dialect='excel')
        wr.writerow(sched)
