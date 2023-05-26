class L33t:

    def __init__(self):
        self.__leet = {
            "a" : 4,
            "e" : 3,
            "i" : 1,
            "o" : 0,
            "l" : 1,
            "s" : 5,
            "b" : 8,
            "t" : 7,
            "z" : 2,
            "g" : 6
        }
    
    def getLeet(self):
        return self.__leet

    def _leetWord(self, word):
        return
    
    def transform (self, word_array):
        leet_array = []
        for word in word_array:
            leetWordArray = L33tFullWord._leetWord(self, word)
            
            leetWordArray.extend(L33tOneLetter._leetWord(self, word))

            for counter, el in enumerate(leetWordArray):
                leet_array.append(el)
        
        return leet_array
    

class L33tFullWord(L33t):
    def __init__(self):
        super().__init__()

    def _leetWord(self, word):
        leet_array = []
        fullWord = word

        for index, letter in  enumerate(fullWord):
            letter = letter.lower()

            for leetLetter in self.getLeet():
                if (leetLetter == letter):
                    fullWord = fullWord[:index] + str(self.getLeet()[leetLetter]) + fullWord[index+1:]
                    leet_array.append(fullWord)
                    break
        
        return leet_array

class L33tOneLetter(L33t):
    def __init__(self):
        super().__init__()
    
    def _leetWord(self, word):
        leet_array = []
        oneLetterLeetWord = word

        for index, letter in enumerate(word):
            letter = letter.lower()

            for leetLetter in self.getLeet():
                if leetLetter == letter:
                    oneLetterLeetWord = oneLetterLeetWord[:index] + str(self.getLeet()[leetLetter]) + oneLetterLeetWord[index+1:]
                    leet_array.append(oneLetterLeetWord)
                    oneLetterLeetWord = word
                    break
        
        return leet_array