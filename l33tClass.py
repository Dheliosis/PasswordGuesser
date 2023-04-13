class L33t:
    leet = {
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
        # print(word)
        leetArray = []
        cleanWord = word.lower()

        leetArray = self.leetAllWord(cleanWord, leetArray)
        
        leetArray = self.leetOneLetter(cleanWord, leetArray)

        # print('leetArray',leetArray) 
        return leetArray

    def leetAllWord (self, word, leetArray):
        fullWord = word

        for index, letter in  enumerate(fullWord):
            for leetLetter in self.leet:
                if (leetLetter == letter):
                    fullWord = fullWord[:index] + str(self.leet[leetLetter]) + fullWord[index+1:]
                    leetArray.append(fullWord)
                    break
        
        return leetArray

    def leetOneLetter (self, word, leetArray):
        oneLetterLeetWord = word

        for index, letter in enumerate(word):
            for leetLetter in self.leet:
                if index == 0:
                    break
                if leetLetter == letter:
                    oneLetterLeetWord = oneLetterLeetWord[:index] + str(self.leet[leetLetter]) + oneLetterLeetWord[index+1:]
                    leetArray.append(oneLetterLeetWord)
                    oneLetterLeetWord = word
                    break
        
        return leetArray
