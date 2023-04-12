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
        leetArray = []
        word= word.lower()
        print(word)
        for index, letter in  enumerate(word, start=0):
            print(letter)
            for leetLetter in self.leet:
                print(leetLetter, letter)
                if (leetLetter == letter):
                    print('yes')
                    word = word[:index] + str(self.leet[leetLetter]) + word[index+1:]
                    print(word)
                    leetArray.append(word)
                    break
        print(leetArray) 
        return leetArray