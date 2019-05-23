import sys
import random
import string

def genRandStr(CONST_STR):   # print random string of length CONST_STR
    """Return random string of length CONST_STR."""
    ENTRADA  = ''
    for x in range(0, len(CONST_STR)):
        ENTRADA  = ENTRADA  + random.choice(string.ascii_uppercase + string.whitespace)
    return ENTRADA


def compStr(randStr,CONST_STR):   # compare CONST_STR with randStr
    """Return index of ENTRADA  -- number of common characters in ENTRADA  and CONST_STR."""
    randStrIndex = 0
    for i in range(0, len(CONST_STR)):
        if CONST_STR[i] == randStr[i]:
            randStrIndex += 1
    return randStrIndex


def modRandStr(randStr,CONST_STR,CONST_PROB):    # modify each character of ENTRADA  with probability CONST_PROB%
    """Return modified ENTRADA  -- each character of ENTRADA  is modified with probability CONST_PROB%."""
    newRandStr = randStr
    for x in range(0, len(CONST_STR)):
        randInt = random.randint(1, 100)
        if randInt <= CONST_PROB:
            newRandStr = newRandStr[:x] + random.choice(string.ascii_uppercase + string.whitespace) + newRandStr[x + 1:]
    return newRandStr


def Weasel(CONST_STR, SIZE, PROB, ENTRADA):

    CONST_SIZE = int(SIZE)
    CONST_PROB = int(PROB)   
    loopNumber = 0
    strFound = False
    resultList = []
    while not strFound:
        strList = [''] * CONST_SIZE
        indexList = [None] * CONST_SIZE
        for x in range(0, CONST_SIZE):
            strList[x] = modRandStr(ENTRADA,CONST_STR,CONST_PROB)
            indexList[x] = compStr(strList[x],CONST_STR)
        maxIndex = max(indexList)
        if maxIndex == len(CONST_STR):
            strFound = True
        ENTRADA  = strList[indexList.index(maxIndex)]
        resultList.append(str(loopNumber) + ": " + ENTRADA  + " -- score: " + str(maxIndex))
        loopNumber += 1
    return resultList

'''
CONST_STR = "METHINKS IT IS LIKE A WEASEL"
CONST_SIZE = 100
CONST_PROB = 5
ENTRADA  = "cccccccccccccccccccccccccccc"
'''

