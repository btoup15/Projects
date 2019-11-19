#################################
#                               #
#   Author: Benjamin S. Toups   #
#          8/30/2019            #
#                               #
#################################

import os
import numpy as np
import matplotlib.pyplot as plt
import random

os.system('cls')

N = int(input('What is the size of the population? '))
#freqA = float(input('What is the starting frequency of the A allele? '))
freqA = .5
#gens = int(input('How many generations is the population simulated over? '))
gens = 100
#runs = int(input('How many runs should be simulated simultaneously? '))
runs = 5

# Creating the random numbe generator that will be used to generate
# the starting population as well as select individuals to breed
def randnum():
    num1 = random.randint(1, (2 ** 15 - 1))
    num2 = random.randint(1, (2 ** 15 - 1))
    numer = (num1 * 32768) + num2
    choice = numer / 1073741823
    return choice

# selects a parent from the population
def PickParents():
    num = (randnum() * N) // 1
    return num

# Generates individuals based on an initial frequency
def GenIndiv():
    first = randnum()
    if first <= freqA:
        first = 1
    else:
        first = 0
    second = randnum()
    if second <= freqA:
        second = 1
    else:
        second = 0
    if first + second == 2:
        return "AA"
    elif first + second == 1:
        return "Aa"
    else:
        return "aa"

# calculates the allele frequencies of a population
def calcFreqs(pops):
    A = 0
    for i in pops:
        if i == 'AA':
            A += 2
        elif i == 'Aa' or i == 'aA':
            A += 1
        else:
            pass
    frequency = A / (N * 2)
    return frequency

finalfreqs = []   #the list that will contain the final frequencies of each run
for i in range(runs):
    g = 1
    indivs = []
    freqs = []
    for i in range(N):   # generates an initial population
        indivs.append(GenIndiv())
    freqs.append(calcFreqs(indivs))
    while g != gens:    # iteratively calculates p(A) for each generation
        newGen = []
        for i in range(N):
            first = int(PickParents())
            second = int(PickParents())
            while first == second:
                second = int(PickParents())
            firstparent = indivs[first]
            secondparent = indivs[second]
            ran1 = randnum()
            if ran1 < .5:
                firstgamete = firstparent[0]
            else:
                firstgamete = firstparent[1]
            ran2 = randnum()
            if ran2 < .5:
                secondgamete = secondparent[0]
            else:
                secondgamete = secondparent[1]
            newAllele = firstgamete + secondgamete
            newGen.append(newAllele)
        freqs.append(calcFreqs(newGen))
        indivs = newGen
        g += 1
    finalfreqs.append(freqs[-1])
    #plt.plot(range(gens), freqs)
print(finalfreqs)
# plt.xlabel('Generation')
# plt.ylabel('p(A)')
# plt.ylim(0, 1)
# plt.xlim(0, gens)
# plt.show()
