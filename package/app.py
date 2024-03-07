from tkinter import simpledialog, messagebox

from package.diaries import Diaries


class Main:
    def __init__(self):
        self.__diary = None
        self.diaries = Diaries()

    def start(self):
        self.__print_message("Welcome!")
        user_choice = messagebox.askyesno("Create Diary", "Would you like to create a new diary?")
        if user_choice:
            self.create_diary()

        self.goto_main_menu()

    def goto_main_menu(self):
        main_menu = """
        Welcome!
        What do you want to do today?
        1-> Create A Diary
        2-> unlock
        3-> Add Entry
        4-> Update Entry
        5-> Find Entry
        6-> Delete Entry!!!
        7-> Exit
        
        Select an option: 
        """
        user_choice = self.__user_input(main_menu, "Main Menu")
        if user_choice:
            self.check_user_choice(user_choice)

    def check_user_choice(self, user_choice: str):
        if user_choice == "1":
            self.create_diary()
        elif user_choice == "2":
            self.unlock()
        elif user_choice == "3":
            self.add_entry()
        elif user_choice == "4":
            self.update_entry()
        elif user_choice == "5":
            self.find_entry()
        elif user_choice == "6":
            self.delete_entry()
        elif user_choice == "7":
            self.exit()
        else:
            self.goto_main_menu()

    def create_diary(self):
        username = self.__user_input('Enter your username: ', 'Create diary')
        password = self.__user_input('Enter your password: ', 'Create diary')
        self.diaries.add_diary(username, password)
        self.__print_message("Welcome  to your diary " + username)
        self.goto_main_menu()

    def lock(self):
        self.__diary.lock_diary()
        self.__print_message("You are now locked")
        self.goto_main_menu()

    def unlock(self):
        try:
            password = self.__user_input('Enter your password: ', "password")
            self.__diary.unlock_diary(password)
            self.__print_message('You have successfully unlocked your diary')
            self.goto_main_menu()
        except Exception as e:
            self.__print_message(str(e))
        finally:
            self.goto_main_menu()

    def add_entry(self):
        username = self.get_username()
        self.diaries.find_by_username(username)

        title = input('Enter your title: ')
        body = input('Enter your body: ')
        try:
            self.__diary.create_entry(title, body)
            self.__print_message(self.__diary.id_number)
            self.__print_message('Entry saved!')
        except ValueError as e:
            self.__print_message(str(e))
        finally:
            self.goto_main_menu()

    def update_entry(self):
        try:
            id_number = input('Confirm your id number: ')
            new_title = input('Enter your new title: ')
            new_body = input('Enter your new body: ')
            self.__diary.update_entry((int(id_number)), new_title, new_body)
            self.__print_message('You have successfully updated your entry')
        except Exception as e:
            self.__print_message(str(e))
        finally:
            self.goto_main_menu()

    def find_entry(self):
        try:
            id_number = input('What is the Id number of the entry you would like to find: ')
            entry = self.__diary.find_entry(int(id_number))
            self.__print_message(entry)
        except Exception as e:
            self.__print_message(str(e))
        finally:
            self.goto_main_menu()

    def delete_entry(self):
        id_number = self.__user_input('What is the Id number of the entry you would like to delete: ', 'delete')
        try:
            self.__diary.delete_entry(int(id_number))
            self.__print_message("You have successfully deleted an entry")
        except Exception as e:
            self.__print_message(str(e))
        finally:
            self.lock()
            self.goto_main_menu()

    @staticmethod
    def __print_message(message: str):
        messagebox.showinfo("Message", message)

    @staticmethod
    def exit():
        print("Exiting application...")
        exit()

    def get_username(self):
        return self.__user_input('Enter your username: ', 'Username')

    @staticmethod
    def __user_input(prompt: str, title: str) -> str:
        return simpledialog.askstring(title, prompt)


user: Main = Main()
if __name__ == "__main__":
    user.start()
