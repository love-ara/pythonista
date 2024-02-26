from account_and_bank.bank import Bank


class BankApp:
    def __init__(self):
        self.bank = Bank("Aramide Bank")

    def goto_main_menu(self):
        main_menu = """
            Welcome to This bank App!
            What do you want to do today?
            1-> Create Account
            2-> Withdraw
            3-> Deposit
            4-> Transfer
            5-> Check Balance
            6-> Close Account
            7-> Exit App!!!
            """
        user_input = input(main_menu)
        option = user_input[0]
        if option == '1':
            self.create_account()
        elif option == '2':
            self.withdraw()
        elif option == '3':
            self.deposit()
        elif option == '4':
            self.transfer()
        elif option == '5':
            self.check_balance()
        elif option == '6':
            self.close_account()
        elif option == '7':
            self.exit_app()
        else:
            self.goto_main_menu()

    def check_balance(self):
        account_number = input("Enter your account number: ")
        pin = input("Enter your pin: ")
        try:
            balance = self.bank.check_balance(int(account_number), pin)
            print("Your balance is:", balance)
        except BaseException as e:
            print(e)
        finally:
            self.goto_main_menu()

    def transfer(self):
        amount = input("Enter transfer amount: ")
        sender_account = input("Enter your account number: ")
        receiver_account = input("Enter the receiving account number: ")
        pin = input("Enter your pin: ")
        try:
            self.bank.transfer(int(sender_account), int(receiver_account), int(amount), pin)
            print("Transfer successful!")
        except BaseException as e:
            print(e)
        finally:
            self.goto_main_menu()

    def deposit(self):
        account_number = input("Enter your account number: ")
        amount = input("Enter an amount: ")
        try:
            self.bank.deposit(int(account_number), int(amount))
            print("Deposit successful!")
        except BaseException as e:
            print(e)
        finally:
            self.goto_main_menu()

    def withdraw(self):
        account = input("Enter your account number: ")
        amount = input("Enter the amount: ")
        pin = input("Enter your pin: ")
        try:
            self.bank.withdraw(int(account), int(amount), pin)
        except BaseException as e:
            print(e)
        finally:
            self.goto_main_menu()

    def close_account(self):
        account_number = input("Enter the account number: ")
        pin = input("Enter your pin: ")
        try:
            self.bank.remove_account(int(account_number), pin)
            print("Account closed successfully!")
        except BaseException as e:
            print(e)
        finally:
            self.exit_app()

    def create_account(self):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        pin = input("Enter your pin: ")
        new_account = self.bank.register_customer(first_name, last_name, pin)
        print("Account created successfully!")
        print(f"Your account number is: {self.bank.get_account_number(new_account)}")
        self.goto_main_menu()

    @staticmethod
    def exit_app():
        print("Exiting application...")
        exit()


ara_bank: BankApp = BankApp()
if __name__ == "__main__":
    ara_bank.goto_main_menu()
