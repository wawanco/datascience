from learn_pypkg.review.wordcount import WordCount


def replace_word(filename):
    with open(filename) as fin:
        with open('new_alice.txt', 'w') as fout:
            for line in fin:
                new_line = line.rstrip().replace('Alice', 'Dora')
                print(new_line)
                fout.write(new_line)


if __name__ == "__main__":
    replace_word('alice.txt')
    wc = WordCount('new_alice.txt')
    wc.print_count()
