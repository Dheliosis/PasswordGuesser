# import unicode

class Word:
    @staticmethod
    def transform():
        return

class Capitalize(Word):
    @staticmethod
    def transform(word):
        return word.capitalize()

class Uppercase(Word):
    @staticmethod
    def transform(word):
        return word.upper()

class Lowercase(Word):
    @staticmethod
    def transform(word):
        return word.lower()