import unittest
from learn_pypkg.review.wordcount import WordCount

wc_obj = WordCount('fixtures/alice.txt')


class Test(unittest.TestCase):
    wc = ('Words:', 274)
    sc = ('Sentences:', 7)
    cc = ('Letters:', 1120)

    def test_wc(self):
        self.assertCountEqual(wc_obj.word_count(), self.wc)

    def test_sentences(self):
        self.assertEqual(wc_obj.sentence_count(), self.sc)

    def test_characters(self):
        self.assertEqual(wc_obj.letter_count(), self.cc)


if __name__ == '__main__':
    unittest.main()
