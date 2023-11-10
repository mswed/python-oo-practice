"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Class to pick a random word from a file
    >>> finder = WordFinder('/home/mswed/Documents/Coding/Springboard/Python/oop/python-oo-practice/words.txt')
    235886 words read
    >>> type(finder)
    <class 'wordfinder.WordFinder'>
    >>> random.seed(1)
    >>> finder.random()
    'choler'
    >>> finder.random()
    'pneumodynamics'
    >>> finder.random()
    'unrulableness'

    >>> finder = SpecialWordFinder('/home/mswed/Documents/Coding/Springboard/Python/oop/python-oo-practice/other_words.txt')
    4 words read
    >>> type(finder)
    <class 'wordfinder.SpecialWordFinder'>
    >>> random.seed(1)
    >>> finder.random()
    'parsnips'
    >>> finder.random()
    'kale'
    >>> finder.random()
    'apple'
    """

    def __init__(self, path):
        """
        Initialize the WordFinder
        @param path: str, path to a file containing the words
        """

        self.path = path
        self.words = self.load_file()
        print(f'{len(self.words)} words read')

    def __repr__(self):
        return f'<WordFinder path={self.path}>'

    def load_file(self):
        words = []
        with open(self.path, 'r') as input_file:
            for word in input_file:
                words.append(word.strip())

        return words

    def random(self):
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    def __init__(self, path):
        super().__init__(path)

    def load_file(self):
        words = super().load_file()
        return [word for word in words if not word.startswith('#') and word != '']


