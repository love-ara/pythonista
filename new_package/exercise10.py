def separate_strings(str1, str2):
    firstStr = str1.replace(str1[-1], str2[-1])
    secondStr = str2.replace(str2[-1], str1[-1])

    return ''.join(secondStr) + ' '+ (firstStr)

def swap_char(str1, str2):
    return str2[:2] + str1[2:]+ " " + str1[:2] + str2[2:]

print(separate_strings('abc', 'xyz'))
print(swap_char('aramide', 'ayomide'))