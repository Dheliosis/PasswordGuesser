from wordClass import Word
from dateClass import Date
from itertools import combinations
from datetime import datetime
from l33tClass import L33tFullWord
from l33tClass import L33tOneLetter

class WordProcessor:
    def __init__(self, array):
        self.wordClass = Word()
        self.dateClass = Date()
        self.l33tFullWord = L33tFullWord()
        self.l33tOneLetter = L33tOneLetter()
        self.initiale_word_array = ['Elisa', 'Jason','mystere', '2023-04-06']
        self.case_word_array = []
        self.options = {
            "leet": True,
            "capitalize": True,
            "lowercase": True,
            "uppercase": True,
            "transformDate": True
        }
        self.passwords = self.process(array)

    def process(self, array):
        self.initiale_word_array = array.copy()
        word_array_copy = self.initiale_word_array.copy()

        print(word_array_copy)

        
        if self.options["transformDate"]:
            word_array_copy = self.transformDate(word_array_copy)
            


        for word in word_array_copy:
            if self.options["capitalize"]:
                self.case_word_array.append(self.wordClass.capitalize(word))
            if self.options["lowercase"]:
                self.case_word_array.append(self.wordClass.lowercase(word))
            if self.options["uppercase"]:
                self.case_word_array.append(self.wordClass.uppercase(word))


        temporary_word_array = self.deleteDuplicate(self.case_word_array)
        temporary_word_array.extend(self.initiale_word_array)

        if self.options["leet"]:
            temporary_word_array.extend(self.transformLeet(temporary_word_array))


        clean_word_array = self.deleteDuplicate(temporary_word_array)
        print(clean_word_array)

        result = []
        for i in range(1, 6):
            for combo in combinations(clean_word_array, i):
                result.append(self.transform_to_string(combo))

        return result

    def transform_to_string(self, combo):
        str = ''
        for item in combo:
            str = str + item

        return str

    def deleteDuplicate (self,word_array):
        temporary = []
        for item in word_array:
            if item not in temporary:
                temporary.append(item)

        return temporary

    # A transformer et à mettre dans la class de date
    # Envoyer le initiale_word_arry par les paramêtres de la fonction
    # Et transformer les self.dateClass.function and self.function
    def transformDate (self, exitArray):
        for word in self.initiale_word_array:
            try:
                datetime.strptime(word, '%Y-%m-%d')
                date_clean = self.dateClass.cleanDate(word)
                for date in date_clean:
                    exitArray.append(date)
                month = self.dateClass.transformMonth(date_clean[1])
                for el in month:
                    exitArray.append(str(el))
            except ValueError:
                False

        return exitArray

    # A transformer et à mettre dans la class de leet
    def transformLeet (self, word_array):
        leet_array = []
        for word in word_array:
            leetWordArray = self.l33tFullWord.leetWord(word)
            
            leetWordArray.extend(self.l33tOneLetter.leetWord(word))

            for counter, el in enumerate(leetWordArray):
                leet_array.append(el)
        
        return leet_array