from package.diaries import Diaries
from package.diary import Diary


class Main:
    def __init__(self):
        self.diary = Diary('username', 'password')
        self.diaries = Diaries()

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
        """
        user_input = input(main_menu)
        option = user_input[0]
        if option == '1':
            self.create_diary()
        elif option == '2':
            self.unlock()
        elif option == '3':
            self.add_entry()
        elif option == '4':
            self.update_entry()
        elif option == '5':
            self.find_entry()
        elif option == '6':
            self.delete_entry()
        elif option == '7':
            self.exit()
        else:
            self.goto_main_menu()

    def create_diary(self):
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        self.diaries.add_diary(username, password)
        print("Welcome  to your diary " + username)
        self.goto_main_menu()

    def find_diary_by_username(self):
        try:
            username = input('Enter your username: ')
            self.diaries.find_by_username(username)
        except Exception as e:
            print(e)
        finally:
            self.goto_main_menu()

    def lock(self):
        self.diary.lock_diary()
        print("You are now locked")
        self.goto_main_menu()

    def unlock(self):
        try:
            password = input('Enter your password: ')
            self.diary.unlock_diary(password)
            print('You have successfully unlocked your diary')
            self.goto_main_menu()
        except Exception as e:
            print(e)
        finally:
            self.goto_main_menu()

    def add_entry(self):
        title = input('Enter your title: ')
        body = input('Enter your body: ')
        self.diary.create_entry(title,  body)
        print(self.diary.id_number)
        print('Entry saved!')
        self.lock()

    def update_entry(self):
        id_number = input('Confirm your id number: ')
        new_title = input('Enter your new title: ')
        new_body = input('Enter your new body: ')
        self.diary.update_entry((int(id_number)), new_title, new_body)
        print('You have successfully updated your entry')
        self.goto_main_menu()

    def find_entry(self):
        id_number = input('What is the Id number of the entry you would like to find: ')
        try:
            entry = self.diary.find_entry(int(id_number))
            print(entry)
        except Exception as e:
            print(e)
        finally:
            self.goto_main_menu()

    def delete_entry(self):
        id_number = input('What is the Id number of the entry you would like to delete: ')
        try:
            self.diary.delete_entry(int(id_number))
            print("You have successfully deleted an entry")
        except Exception as e:
            print(e)
        finally:
            self.lock()
            self.goto_main_menu()

    @staticmethod
    def exit():
        print("Exiting application...")
        exit()


user: Main = Main()
if __name__ == "__main__":
    user.goto_main_menu()
