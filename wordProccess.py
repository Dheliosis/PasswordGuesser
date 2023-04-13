from wordClass import Word
from dateClass import Date
from l33tClass import L33t
from itertools import combinations
from datetime import datetime

class WordProcessor:
    wordClass = Word()
    dateClass = Date()
    leetClass = L33t()

    def __init__(self):
        self.initiale_word_array = ['Elisa', 'Jason','mystere', '2023-04-06']
        self.case_word_array = []
        self.passwords = []
        self.options = {
            "leet": True,
            "capitalize": True,
            "lowercase": True,
            "uppercase": True,
            "transformDate": True
        }

    def process(self, array):
        self.initiale_word_array = array.copy()
        word_array_copy = self.initiale_word_array.copy()

        print(word_array_copy)

        for word in self.initiale_word_array:
            if self.options["transformDate"]:
                try:
                    datetime.strptime(word, '%Y-%m-%d')
                    date_clean = self.dateClass.cleanDate(word)
                    for date in date_clean:
                        word_array_copy.append(date)
                    month = self.dateClass.transformMonth(date_clean[1])
                    for el in month:
                        word_array_copy.append(str(el))
                except ValueError:
                    False


        for word in word_array_copy:
            if self.options["capitalize"]:
                self.case_word_array.append(self.wordClass.capitalize(word))
            if self.options["lowercase"]:
                self.case_word_array.append(self.wordClass.lowercase(word))
            if self.options["uppercase"]:
                self.case_word_array.append(self.wordClass.uppercase(word))


        temporary_word_array = self.deleteDuplicate(self.case_word_array)
        temporary_word_array.extend(self.initiale_word_array)

        leet_array = []
        for word in temporary_word_array:
            if self.options["leet"]:
                print(word)
                leet = self.leetClass.leetWord(word)
                print(leet)
                for counter, el in enumerate(leet):
                    leet_array.append(el)

        temporary_word_array.extend(leet_array)

        clean_word_array = self.deleteDuplicate(temporary_word_array)
        print(clean_word_array)

        for i in range(1, 6):
            for combo in combinations(clean_word_array, i):
                self.passwords.append(self.transform_to_string(combo))

        return self.passwords

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
