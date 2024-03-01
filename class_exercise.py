class Exercise:
    def __init__(self):
        self.data = ""

    def getString(self):
        self.data = input("Enter a string: ")

    def printString(self):
        return self.data.upper()

    def __repr__(self):
        return f'{self.printString()}'


ara = Exercise()
ara.getString()
print(ara.printString())