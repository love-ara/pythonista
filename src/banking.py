class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def show_details(self):
        return f"Thank you. {self.name.title()}"


class Bank(User):
    total_deposit = 0
    total_withdraws = 0

    def __init__(self, name, balance):
        super().__init__(name)
        self.balance = balance

    def show_info(self):
        return f'{self.name} has a balance of: (round{self.balance, 2})

    def deposit(self):
        dp = float(input(f"{self.name.title()}, please enter how much you would like to deposit: "))
        print("Amount successfully deposited!")
        self.balance += dp
        self.total_deposit += 1
        return f"Your balance is now: (round{self.balance, 2})"

    def withdraw(self):
        wd = float(input(f"{self.name.title()}, please enter how much you would like to withdraw: "))
        if self.balance < wd:
            return f"you can't withdraw {wd}!"
        else:
            print("Withdraw successfully!")
            self.balance += wd
            self.total_withdraws += 1

    def options(user_two):
        print("Thank you for creating an account with us!")
        print("There are a list of options, please choose the number you want")
        while True:
            option_choice = int(input(
                "1. Check balance\n2. Withdraw\n3. Deposit\n4. Total withdraws\n5. Total deposits\n6. Exit\n"))
            if option_choice == 1:
                print(user_two_bank.show_details())
                if option_choice == 1 and user_two is not None:
                    print(user_two.bank.show_details())
            elif option_choice == 2:
                print(user_two.bank.withdraw())
                if option_choice == 2 and user_two is not None:
                    wd = input(f"{user_two.name} would you like to withdraw? Yes or No?")
                    if wd.lower() == 'yes':
                        print(user_two.bank.withdraw())
            elif option_choice == 3:
                print(user_two.bank.deposit())
                if option_choice == 3 and user_two is not None:
                    wd = input(f"{user_two.name} would you like to deposit?  Yes or No?")
                    if wd.lower() == 'yes':
                        print(user_two.bank.deposit())
            elif option_choice == 4:
                print(f"There have been {user_two.total_withdraws} withdraws!")
                if option_choice == 4 and user_two is not None:
                    print(f"There have been {user_two.bank.total_withdraws} withdraws!")
            elif option_choice == 5:
                print(f"There have been {user_two.bank.total_deposits} deposits!")
                if option_choice == 5 and user_two is not None:
                    print(f"There have been {user_two.bank.total_deposits} deposits!")
            elif option_choice == 6:
                print(f"Thank you for using this bank")
                return False
                break
            else:
                print("Please enter a valid number on the list ")


def bank_creation(name):
    b



