import re
import sys


class WordCount:
    """Conducts character, word, and letter count of object"""

    def __init__(self, filename) -> None:
        self.filename = filename

    def open_file(self):
        """Opens a file object to be used across the class"""
        with open(self.filename, 'r') as file:
            file_contents = file.read()
            return file_contents

    def word_count(self):
        file_contents = self.open_file()
        return 'Words:', len(file_contents.split())

    def sentence_count(self):
        file_contents = self.open_file()
        return 'Sentences:', file_contents.count('.') + file_contents.count('!') + file_contents.count('?')

    def letter_count(self):
        """Returns a file's character count, excluding punctuation"""
        letter_counter = 0
        pattern = r'[\W]'  # excluding all punctuation
        cc_file = self.open_file()
        total_words = cc_file.split()
        for word in total_words:
            for letter in word:
                if not re.search(pattern, letter):
                    letter_counter += 1
        return "Letters:", letter_counter

    def print_count(self):
        print(self.word_count(), '\n', self.sentence_count(), '\n', self.letter_count())


if __name__ == '__main__':
    wc = WordCount(sys.argv[1])
    wc.print_count()
