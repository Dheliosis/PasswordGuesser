from cmath import log
import word
import datetime
from itertools import permutations

def main():
    WORD_ARRAY = ['Elisa', 'Jason','mystere']
    WORD_ARRAY = detectType(WORD_ARRAY)
    result = []

    workArray = []

    for word in WORD_ARRAY:
        workArray.append(word)

        newWorkArray = []
        for word in workArray:
            newWorkArray.append(lowercase(word))

        result = result + randomWord(newWorkArray)

        newWorkArray = []
        for word in workArray:
            newWorkArray.append(uppercase(word))

        result = result + randomWord(newWorkArray)

        newWorkArray = []
        for word in workArray:
            newWorkArray.append(capitalize(word))

        result = result + randomWord(newWorkArray)

    print(result)

# commun
def detectType(WORD_ARRAY):
    newWORD_ARRAY = []
    for word in WORD_ARRAY:
        if isinstance(word, str):
            print ('string')
        elif isinstance(word, datetime.date):
            word = cleanDate(word)
            print(word)
        newWORD_ARRAY.append(word)
        
        
    print (newWORD_ARRAY)
    return newWORD_ARRAY

# Word
def capitalize(word):
    return word.capitalize()

def uppercase(word):
    return word.upper()

def lowercase(word):
    return word.lower()

def randomWord (array):
    print('[randomWord]')
    result = []
    for y in permutations(array):
        result.append(convertTuple(y))

    return result

def convertTuple(tup):
    str = ''
    for item in tup:
        str = str + item

    return str



# Date
def cleanDate(date):
    print('[cleanDate]')
    date= str(date)
    dateArray = date.split('-')
    print(dateArray)
    delemiter = ''
    return delemiter.join(dateArray)


month= {
    "01": [1,'01', 'janvier', 'janv'],
    "02": [2,'02', 'février', 'fevr'],
    "03": [3,'03', 'mars', 'mars'],
    "04": [4,'04', 'avril', 'avr'],
    "05": [5,'05', 'mai', 'mai'],
    "06": [6,'06', 'juin', 'juin'],
    "07": [7,'07', 'juillet', 'juill'],
    "08": [8,'08', 'aout', 'aout'],
    "09": [9,'09', 'septembre', 'sept'],
    "10": [10,'10', 'octobre', 'oct'],
    "11": [11,'11', 'novembre', 'nov'],
    "12": [12,'12', 'decembre', 'dec'],
}

main()