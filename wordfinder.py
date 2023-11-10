"""Word Finder: finds random words from a dictionary."""
from random import choice


class WordFinder:
    """Class to pick a random word from a file"""

    def __init__(self, path):
        """
        Initialize the WordFinder
        @param path: str, path to a file containing the words
        """

        self.path = path
        self.words = self.load_file()
        print(f'{len(self.words)} words read')

    def load_file(self):
        words = []
        with open(self.path, 'r') as input_file:
            for word in input_file:
                words.append(word.strip())

        return words

    def random(self):
        print(choice(self.words))


class SpecialWordFinder(WordFinder):
    def __init__(self, path):
        super().__init__(path)

    def load_file(self):
        words = super().load_file()
        return [word for word in words if not word.startswith('#') and word != '']

# finder = WordFinder('/home/mswed/Documents/Coding/Springboard/Python/oop/python-oo-practice/words.txt')
# finder.random()

finder = SpecialWordFinder('/home/mswed/Documents/Coding/Springboard/Python/oop/python-oo-practice/other_words.txt')
finder.random()
