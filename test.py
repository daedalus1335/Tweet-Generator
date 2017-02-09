import random

test_file = ("/usr/share/dict/words")

num_lines = 0
num_words = 0
num_chars = 0

def get_words(test_file, word_amount):

    for num in word_amount:
        (random.randrange(0, word_amount))

if __name__ == '__main__':
    with open(test_file, 'r') as f:
        for line in f:
            words = line.split()

            num_lines += 1
            num_words += len(words)
            num_chars += len(line)

    get_words(test_file, num_words)
