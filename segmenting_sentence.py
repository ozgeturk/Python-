

sentence = input()
punctuation = "!\"#$%&'()*+,-./:;<=>?@[\]^`{|}~"
suffixes = ["acy", "ance", "ence", "dom", "er", "or", "ism", "ist",
             "ty", "ment", "ness", "ship", "sion", "tion", "ate",
            "en", "fy", "ize", "able", "ible", "al",
            "esque", "ful", "ic", "ous", "ish", "ive",
            "less", "ed", "ing", "ly", "ward", "wise"]

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
def segment(sentence):
    for word in sentence:
        for punc in punctuation:
            if word.endswith(punc):
                sentence = sentence.replace(word, " " + word + " ")

    s_sentence = sentence.split()

    for i in s_sentence:
        for j in suffixes:
            if i.endswith(j):
                i = i.replace(i, i[:-len(j)] + "_" + j)

    return s_sentence

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

if "_" in sentence:
    print(desegment(sentence))
else:
    word_list = segment(sentence)
    print(" ".join(word_list))

