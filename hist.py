def histogram(source_text):
    histogram = {}
    for word in source_text.split():
        //get rid of periods and colons
        word = re.sub('[.,:]', '',word)

        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] += 1
    return histogram
