######################
#   Author: Ben Toups
#   1/17/2020
######################
import os
import numpy as np

os.system('cls')
inpt = str(input("Enter the filepath of the text file: "))

text = open(inpt, encoding='utf8').read()
iso = text.split()

def make_pairs(lst):
    for i in range(len(lst)-1):
        yield (lst[i], lst[i + 1])
pairs = make_pairs(iso)

word_dict = {}
for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

first_word = np.random.choice(iso)
while first_word.islower():
    first_word = np.random.choice(iso)

chain = [first_word]
n_words = 30

for i in range(n_words):
    chain.append(np.random.choice(word_dict[chain[-1]]))
print(' '.join(chain))
