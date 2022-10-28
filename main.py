from wordClass import Word
from dateClass import Date
from l33tClass import L33t
import datetime
from itertools import permutations
from datetime import datetime
import random

def main():
    wordClass = Word()
    dateClass = Date()
    WORD_ARRAY = ['Elisa', 'Jason','mystere']
    dateClean = dateClass.cleanDate(datetime.now().strftime("%Y-%m-%d"))
    print(dateClean)
    for date in dateClean:
        WORD_ARRAY.append(date)

        
    month = dateClass.transformMonth(dateClean[1])
    result = []
    for el in month:
        # WORD_ARRAY.append(month[random.randint(0, month.__len__()-1)])
        WORD_ARRAY.append(el)
    
        print(WORD_ARRAY)
        WORD_ARRAY = detectType(WORD_ARRAY)

        workArray = []


        for word in WORD_ARRAY:
            workArray.append(word)
            if workArray.__len__() > 5:
                workArray.pop(random.randint(0, 3))
            
            newWorkArray = []
            for word in workArray:
                newWorkArray.append(wordClass.lowercase(word))

            result = result + randomWord(newWorkArray)

            newWorkArray = []
            for word in workArray:
                newWorkArray.append(wordClass.uppercase(word))

            result = result + randomWord(newWorkArray)

            newWorkArray = []
            for word in workArray:
                newWorkArray.append(wordClass.capitalize(word))

            result = result + randomWord(newWorkArray)
            
        WORD_ARRAY.remove(el)

    print(result.__len__())

# commun
def detectType(WORD_ARRAY):
    dateClass = Date()
    
    newWORD_ARRAY = []
    for word in WORD_ARRAY:
        if isinstance(word, str):
            print ('string')
        elif isinstance(word, datetime.date):
            word = dateClass.cleanDate(word)
        newWORD_ARRAY.append(word)
        
        
    print (newWORD_ARRAY)
    return newWORD_ARRAY

# Word

def randomWord (array):
    result = []
    for y in permutations(array):
        result.append(convertTuple(y))

    return result

def convertTuple(tup):
    str = ''
    for item in tup:
        str = str + item

    return str


main()