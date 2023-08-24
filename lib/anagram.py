# your code goes here!
class Anagram():
    def __init__(self, word):
        self.word = word

    def match(self, anagramsList):
        anagrams = []
        for word in anagramsList:
            if sorted(word.lower()) == sorted(self.word.lower()) and word.lower() != self.word.lower():
                anagrams.append(word)
        return anagrams

