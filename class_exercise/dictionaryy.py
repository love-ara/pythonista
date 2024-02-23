sentence = "The palace is few miles away from the village but going to the palace is cool and fun"


def sentences_to_dict(sentence1):
    sentence_list = sentence1.lower().split()
    sentence_dictionary = {}

    for item in sentence_list:
        if item in sentence_dictionary:
            sentence_dictionary[item] += 1
        else:
            sentence_dictionary[item] = 1
    return sentence_dictionary


print(sentences_to_dict(sentence))
