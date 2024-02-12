
def count_words(text):
    word = {}

    for letter in text:
        counter = 0
        for letter1 in text:
            if letter == letter1:
             counter += 1
        word[letter] = counter
    return word

sample = 'google.com'

print({k: sample.count(k) for k in sample})
print(count_words(sample))
print(count_words("google.com"))