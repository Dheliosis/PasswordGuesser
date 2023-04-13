class L33t:

    def __init__(self):
        self.leet = {
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

    def leetWord(self, word):
        return
    

class L33tFullWord(L33t):
    def __init__(self):
        super().__init__()

    def leetWord(self, word):
        leet_array = []
        fullWord = word

        for index, letter in  enumerate(fullWord):
            letter = letter.lower()

            for leetLetter in self.leet:
                if (leetLetter == letter):
                    fullWord = fullWord[:index] + str(self.leet[leetLetter]) + fullWord[index+1:]
                    leet_array.append(fullWord)
                    break
        
        return leet_array

class L33tOneLetter(L33t):
    def __init__(self):
        super().__init__()
    
    def leetWord(self, word):
        leet_array = []
        oneLetterLeetWord = word

        for index, letter in enumerate(word):
            letter = letter.lower()

            for leetLetter in self.leet:
                if leetLetter == letter:
                    oneLetterLeetWord = oneLetterLeetWord[:index] + str(self.leet[leetLetter]) + oneLetterLeetWord[index+1:]
                    leet_array.append(oneLetterLeetWord)
                    oneLetterLeetWord = word
                    break
        
        return leet_array