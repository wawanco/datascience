import sys

if __name__ == '__main__':
    from review.wordcount import WordCount
    wc = WordCount(sys.argv[1])
    wc.print_count()
