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
    
    def transformWord(self, word):
        word= word.lower()
        print(word)
        for i in enumerate(word, start=0):
            for index, letter in  enumerate(word, start=0):
                # print(index, letter)
                index = index + i
                for leetLetter in self.leet:
                    print(leetLetter, letter)
                    if (leetLetter == letter):
                        print('yes')
                        word = word[:index] + str(self.leet[leetLetter]) + word[index+1:]
                        print(word)
                        break
            print(word)