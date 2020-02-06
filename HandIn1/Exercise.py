import math
import itertools
from itertools import product
# 1
names = ['Hans', 'Lars', 'Henrik', 'Lotte', 'Biver', 'Jens', 'Otto']

# A


def returnNamesWithH():
    hNames = []
    for name in names:
        if 'h' in name.lower():
            hNames.append(name)

    return hNames

# B


def createList():
    return range(100**3)

# C


def returnTuples():
    lengths = []
    nameTuple = []
    for n in names:
        lengths.append(len(n))
        nameTuple.append(n)
    return lengths, names
# D


def returnNumericChars():
    string = 'adewtwersd1224tsdfae145dfs124'
    numbers = ''
    for i in range(len(string)):
        if string[i].isdigit():
            numbers += string[i]
    return numbers

# E


def returnAllDiceCombinations():
    dice = {'1', '2', '3', '4', '5', '6'}
    return list(itertools.combinations(range(1, len(dice)+1), 2))
# 2
# A
def createDictionary():
    nameDicts = []
    for n in names:
        nameDict = {}
        nameDict['name'] = n
        nameDict['length'] = len(n)
        nameDicts.append(nameDict)
    return nameDicts
    
# B
def createNumberDictionary():
    numbers = [1,2,3,4,5,6,7,8,9,]
    numberDicts = []
    for n in numbers:
        numberDict = {}
        numberDict['key'] = n
        numberDict['value'] = math.sqrt(n)
        numberDicts.append(numberDict)
    return numberDicts

# 3
def createDiceCombinationDictionary():
    dice = [1,2,3,4,5,6]
    faces = 10
    choices = list(product(range(1, len(dice)+1), repeat=2))
    sums = []
    for c in choices:
        sums.append(int(c[0]+c[1]))
        print(c[1])
    sumAmounts = {i:sums.count(i) for i in sums}
    diceDictList = []
    for s in choices:
        diceDict = {}
        diceDict['combo'] = s
        comboSum = int(s[0]+s[1])
        sumAmount = sumAmounts[comboSum]
        chance = sumAmount/len(sums)*100
        diceDict['chance'] = float("{0:.2f}".format(chance))
        diceDictList.append(diceDict)
    return diceDictList


if __name__ == '__main__':
    print(createDiceCombinationDictionary())
