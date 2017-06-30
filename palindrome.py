class Palindrome:

    @staticmethod
    def is_palindrome(word):
        word=word.lower()
        if word == word[::-1]:
            return True
        else:
            word != word[::-1]
            return False

print(Palindrome.is_palindrome('Deleveled'))
