"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self, path):
        self.path = path
        fileContents = open(path)
        self.words = self.parse(fileContents)
        print(f"{len(self.words)} words read")

    def parse(self, fileContents):
        words = []
        for word in fileContents:
            words.append(word.strip())
        
        return words

    def random(self):
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    def parse(self, fileContents):
        words = []
        for word in fileContents:
            if word.strip() and not word.startswith("#"):
                words.append(word.strip())
        return words
