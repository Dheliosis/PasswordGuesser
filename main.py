from wordClass import Word
from dateClass import Date
from l33tClass import L33t
import datetime
from itertools import permutations
from datetime import datetime
import random

def main():
    # print(form)
    # Bien faire attention au lower upper capitalize pour le leet
    # idée: envoyer au leet la liste qu'on génère à la fin
    wordClass = Word()
    dateClass = Date()
    leetClass = L33t()

    WORD_ARRAY = ['Elisa', 'Jason','mystere', '2023-04-06']
    newWORD_ARRAY = WORD_ARRAY.copy()

    for counter,mot in enumerate(WORD_ARRAY):
        print(mot)
        if not "-" in mot and not isinstance(mot, tuple):
            print("ins", mot)
            leet = leetClass.transformWord(mot)
            for counter, el in enumerate(leet):
                newWORD_ARRAY.append(el)

        elif "-" in mot:
            dateClean = dateClass.cleanDate(mot)
            print(dateClean)
            for date in dateClean:
                newWORD_ARRAY.append(date)
            month = dateClass.transformMonth(dateClean[1])
            print(month)
            for el in month:
                newWORD_ARRAY.append(str(el))
        else:
            print("Ne doit pas se produire", mot)
       
    
    print(WORD_ARRAY)
    print(newWORD_ARRAY)

        
    result = []

    workArray = []


    for word in newWORD_ARRAY:
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

    print(result)
    print(result.__len__())

# commun
def detectType(WORD_ARRAY):
    dateClass = Date()
    print( 'dddd')
    
    newWORD_ARRAY = []
    for word in WORD_ARRAY:
        print(word)
        if isinstance(word, str):
            print ('string')
        elif type(word) is datetime:
            print("date")
            word = dateClass.cleanDate(word)
        elif isinstance(word, int):
            print("int")
            word=str(word)
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