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

pop = int(input('What is the size of the population? '))
freqA = float(input('What is the starting frequency of the A allele? '))


# setting up the random number generator


def randnum():
    num1 = random.randint(1, (2 ** 15 - 1))
    num2 = random.randint(1, (2 ** 15 - 1))
    numer = (num1 * 32768) + num2
    choice = numer / 1073741823
    return choice


# Generating individuals


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


indivs = []

for i in range(pop):
    indivs.append(GenIndiv())
A = 0
a = 0
for i in indivs:
    if i == "AA":
        A += 2
    elif i == "Aa":
        A += 1
        a += 1
    else:
        a += 2
print("Frequency of A is ", (A / (A + a)))
print("Frequency of a is ", (a / (A + a)))
