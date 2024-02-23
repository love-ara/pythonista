from account_and_bank.bank import Bank
from account_and_bank.account_exception import InsufficientFundsException, InvalidPinException, InvalidAmountException


class BankApp:
    gt_bank = Bank("bank")

    @staticmethod
    def goto_main_menu():
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
        user_input = BankApp.input(main_menu)
        option = user_input[0]
        if option == '1':
            BankApp.create_account()
        elif option == '2':
            BankApp.withdraw()
        elif option == '3':
            BankApp.deposit()
        elif option == '4':
            BankApp.transfer()
        elif option == '5':
            BankApp.check_balance()
        elif option == '6':
            BankApp.close_account()
        elif option == '7':
            BankApp.exit_app()
        else:
            BankApp.goto_main_menu()

    @staticmethod
    def check_balance():
        account_number = BankApp.input("Enter your account number: ")
        pin = BankApp.input("Enter your pin: ")
        try:
            balance = BankApp.gt_bank.check_balance(int(account_number), pin)
            print("Your balance is:", balance)
        except Exception as e:
            print(e.get_message())
        finally:
            BankApp.goto_main_menu()

    @staticmethod
    def transfer():
        amount = BankApp.input("Enter transfer amount: ")
        sender_account = BankApp.input("Enter your account number: ")
        receiver_account = BankApp.input("Enter the receiving account number: ")
        pin = BankApp.input("Enter your pin: ")
        try:
            BankApp.gt_bank.transfer(int(sender_account), int(receiver_account), int(amount), pin)
            print("Transfer successful!")
        except Exception as e:
            print(e)
        finally:
            BankApp.goto_main_menu()

    @staticmethod
    def deposit():
        account_number = BankApp.input("Enter your account number: ")
        amount = BankApp.input("Enter an amount: ")
        try:
            BankApp.gt_bank.deposit(int(account_number), int(amount))
            print("Deposit successful!")
        except Exception as e:
            print(e)
        finally:
            BankApp.goto_main_menu()

    @staticmethod
    def withdraw():
        account = BankApp.input("Enter your account number: ")
        amount = BankApp.input("Enter the amount: ")
        pin = BankApp.input("Enter your pin: ")
        try:
            BankApp.gt_bank.withdraw(int(account), int(amount), pin)
        except Exception as e:
            print(e.get_message())
        finally:
            BankApp.goto_main_menu()

    @staticmethod
    def close_account():
        account_number = BankApp.input("Enter the account number: ")
        pin = BankApp.input("Enter your pin: ")
        try:
            BankApp.gt_bank.remove_account(int(account_number), pin)
            print("Account closed successfully!")
        except Exception as e:
            print(e.get_message())
        finally:
            BankApp.exit_app()

    @staticmethod
    def create_account():
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        name = f"{first_name} + " " + {last_name}"
        pin = input("Enter your pin: ")
        number = BankApp.gt_bank.get_account_number()
        new_account = BankApp.gt_bank.register_customer(number, name, pin)
        print("Account created successfully!")
        print("Your account number is:", number)
        BankApp.goto_main_menu()

    @staticmethod
    def exit_app():
        print("Exiting application...")
        exit()

    @staticmethod
    def input(prompt):
        print(prompt)
        return input()

    @staticmethod
    def print_output(output):
        print(output)


BankApp.goto_main_menu()
