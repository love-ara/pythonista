name1 = "bolaji"
name2 = "chichi"
name3 = "DAYO"

sentence = 'welcome to semicolon africa'
print(sentence.replace('c', 'x'))
print(sentence.split(' '))
print(sentence.split('to'))
print(sentence.partition('to'))
names = ['olamide', 'aramide', 'ayomide', 'temide']
print("-".join(names))
print(" ".join(names))



print(name1 == name2)
print(name1 < name2)
print(ord('b')) #ord works with a char 'c', you can get the ascii values of characters with ord

print("o" in name3)

for letter in name3:
    if letter == "a":
        print(letter)

print(name2.replace('chichi','sere'))



#for alignment
print(f'[{name1:10}]')
print(f'[{name1:>10}]')
print(f'[{name1:<10}]')
print(f'[{name1:^10}]')

print(name1 + name2 + name3)
print(f'{name1} {name2}  {name3}')

print(f'{name1 * 5}')

#remove excess space character
name4 = "    muhammed    "
print(len(name4.strip()))
print(name4.strip())


print(name1.upper())
print(name3.lower())
print(name2.capitalize())
print(sentence.title())
print(sentence.casefold())
print(sentence.count('e'))

print(sentence.index('e'))
print(sentence.rindex('e'))
print(sentence.rindex('e', 1, 5))
print(sentence.index('e', 5))

name = input("What is your name?: ").strip()
if name.isalpha():
    print("valid name")
else:
    print("invalid name")


name = input("What is your name?: ").strip()
if name.isalnum():
    print("valid name")
else:
    print("invalid name")

name = input("What is your name?: ").strip()
if name.isascii():
    print("valid name")
else:
    print("invalid name")


name = input("What is your name?: ").strip()
if name.isdigit():
    print("valid name")
else:
    print("invalid name")



for letter in name1:
    pass
else:
    print("invalid")
