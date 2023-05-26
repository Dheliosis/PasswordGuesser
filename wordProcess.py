from wordClass import Capitalize
from wordClass import Uppercase
from wordClass import Lowercase
from dateClass import Date
from itertools import combinations
from datetime import datetime
from l33tClass import L33tFullWord
from l33tClass import L33tOneLetter
from l33tClass import L33t

class WordProcessor:
    def __init__(self, array):
        self.__capitalize = Capitalize()
        self.__uppercase = Uppercase()
        self.__lowercase = Lowercase()
        self.__dateClass = Date()
        self.__l33tFullWord = L33tFullWord()
        self.__l33tOneLetter = L33tOneLetter()
        self.__l33t = L33t()
        self.__initiale_word_array = ['Elisa', 'Jason','mystere', '2023-04-06']
        self.__case_word_array = []
        self.__options = {
            "leet": True,
            "capitalize": True,
            "lowercase": True,
            "uppercase": True,
            "transformDate": True
        }
        self.passwords = self.process(array)

    def process(self, array):
        self.__initiale_word_array = array.copy()
        word_array_copy = self.__initiale_word_array.copy()

        print(word_array_copy)

        
        if self.__options["transformDate"]:
            word_array_copy = self.transformDate(self.__initiale_word_array,word_array_copy)
            


        for word in word_array_copy:
            if self.__options["capitalize"]:
                self.__case_word_array.append(self.__capitalize.transform(word))
            if self.__options["lowercase"]:
                self.__case_word_array.append(self.__lowercase.transform(word))
            if self.__options["uppercase"]:
                self.__case_word_array.append(self.__uppercase.transform(word))


        temporary_word_array = self.__deleteDuplicate(self.__case_word_array)
        temporary_word_array.extend(self.__initiale_word_array)

        if self.__options["leet"]:
            temporary_word_array.extend(self.__l33t.transform(temporary_word_array))


        clean_word_array = self.__deleteDuplicate(temporary_word_array)
        print(clean_word_array)

        result = []
        for i in range(1, 6):
            for combo in combinations(clean_word_array, i):
                result.append(self.__transform_to_string(combo))

        return result

    def __transform_to_string(self, combo):
        str = ''
        for item in combo:
            str = str + item

        return str

    def __deleteDuplicate (self,word_array):
        temporary = []
        for item in word_array:
            if item not in temporary:
                temporary.append(item)

        return temporary

    # A transformer et à mettre dans la class de date
    # Envoyer le initiale_word_arry par les paramêtres de la fonction
    # Et transformer les self.dateClass.function and self.function
    def transformDate (self, initiale_word_array, exitArray):
        return self.__dateClass.transformDate(initiale_word_array, exitArray)
                