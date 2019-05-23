import sys
import random
import string

def genRandStr(CONST_STR):   # gera uma string aleatoria com o mesmo tamanho da string de entrada
    ENTRADA  = ''
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    for x in range(0, len(CONST_STR)):
        ENTRADA  = ENTRADA  + random.choice(alphabet)
    return ENTRADA


def compStr(randStr,CONST_STR):   # compara a string gerada e a target
    randStrIndex = 0
    for i in range(0, len(CONST_STR)):
        if CONST_STR[i] == randStr[i]:
            randStrIndex += 1
    return randStrIndex


def modRandStr(randStr,CONST_STR,CONST_PROB): # modifica os caracteres da entrada utilizando 5% de chance.
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
        print("loop numero: ", loopNumber)
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



