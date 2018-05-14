#!/usr/bin/env python

"""Computes the Colman-Liau index for any given file.
Returns the grade level reading ability of the file.
More on The Colman-Liau Index
https://readable.io/content/the-coleman-liau-index:
Formula:
L = average number of letters per 100 words and;
S = average number of sentences per 100 words.
0.0588L – 0.296S – 15.8
Argv:  filename
"""
import sys

from learn_pypkg.review.wordcount import WordCount

WORD_INCREMENT = 100


def get_letters(wc):
    return wc.letter_count()[1] / wc.word_count()[1] * 100


def get_sentences(wc):
    return wc.sentence_count()[1] / wc.word_count()[1] * 100


def colman_liau(filename):
    wc = WordCount(filename)
    index = 0.0588 * get_letters(wc) - 0.296 * get_sentences(wc) - 15.8
    return "Reading Grade Level of Text:", round(index)


if __name__ == '__main__':
    print(colman_liau(sys.argv[1]))
