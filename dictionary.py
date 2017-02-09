import random
import sys

def open_file(file):
    with open(file) as f:
        corpus = f.read().splitlines()
        f.close()
        return corpus

def random_words(file_array):
    arr2 = []
    arr3 = file_array
    for i in range(int(sys.argv[1])):
        rand_index = random.randint(0, len(arr3) - 1)
        arr2.append(arr3[rand_index])
        arr3.remove(arr3[rand_index])
    return arr2

if __name__ == '__main__':
    text_file = ("/usr/share/dict/words")
    words = open_file(text_file)
    newSentence = random_words(words)
    print " ".join(newSentence)
