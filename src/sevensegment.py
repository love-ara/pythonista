class SevenSegment:
    def __init__(self):
        self.digit = [["  " for _ in range(4)] for _ in range(5)]

    def set_space(self):
        for item in range(5):
            for items in range(4):
                self.digit[item][items] = "  "

    def set_a(self):
        for item in range(4):
            self.digit[0][item] = "# "

    def set_b(self):
        for item in range(3):
            self.digit[item][3] = "# "

    def set_c(self):
        for item in range(2, 5):
            self.digit[item][3] = "# "

    def set_d(self):
        for item in range(4):
            self.digit[4][item] = "# "

    def set_e(self):
        for item in range(2, 5):
            self.digit[item][0] = "# "

    def set_f(self):
        for item in range(3):
            self.digit[item][0] = "# "

    def set_g(self):
        self.digit[2] = ["# " for _ in range(4)]

    def display_segment(self, input_str):
        self.set_space()
        if len(input_str) >= 8 and input_str[7] == '1':
            if input_str[0] == '1':
                self.set_a()
            if input_str[1] == '1':
                self.set_b()
            if input_str[2] == '1':
                self.set_c()
            if input_str[3] == '1':
                self.set_d()
            if input_str[4] == '1':
                self.set_e()
            if input_str[5] == '1':
                self.set_f()
            if input_str[6] == '1':
                self.set_g()
        self.show_segment()

    def show_segment(self):
        for row in self.digit:
            print("".join(row))


def main():
    segment = SevenSegment()
    user_input = input("Enter an 8-character binary input: ")

    if len(user_input) != 8 or not user_input.isdigit() or not all(char in '01' for char in user_input):
        print("Invalid input. Please enter an 8-character binary input.")
        return

    segment.display_segment(user_input)


if __name__ == "__main__":
    main()
