import sys

def open_file(file):
    with open(file) as f:
        words = f.read().split()
        f.close()
    return words

def histogram(words):
    unwanted_chars = """.,-_?""'<>}{)("""
    dictionary = {}
    for raw_word in words:
        word = raw_word.strip(unwanted_chars).lower()
        if word in dictionary:
            dictionary[word] = dictionary[word] + 1
        else:
            dictionary[word] = 1
    return dictionary

def unique_words(words):
    return len(histogram(words))

def frequency(words):
    dictionary = histogram(words)
    inputString = sys.argv[1]
    if inputString in dictionary:
        return dictionary[inputString]

if __name__ == '__main__':
    text_file = '/Users/brandoncontreras/Documents/histTextFile.txt'
    words = open_file(text_file)
    print histogram(words)
    print 'Unique word count: ' + str(unique_words(words))
    print 'That word is found ' + str(frequency(words)) + ' time(s).'
