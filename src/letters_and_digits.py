import re


def countLettersAndDigits(letters):
    new_letter = re.findall("[a-z]", letters)
    new_digit = re.findall("[0-9]", letters)

    return f'LETTER {len(new_letter)} DIGIT {len(new_digit)}'


def count_upperCaseLetters(letters):
    new_letter = re.findall("[A-Z]", letters)
    new_lowercase = re.findall("[a-z]", letters)
    return f'UPPERCASE {len(new_letter)} LOWER CASE {len(new_lowercase)}'



