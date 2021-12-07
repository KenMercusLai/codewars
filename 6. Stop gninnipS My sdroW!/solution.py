def spin_words(sentence):
    return ' '.join([i if len(i) < 5 else i[::-1] for i in sentence.split()])
