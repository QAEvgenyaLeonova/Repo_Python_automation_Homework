'''class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_first_name(self):
        print(self.first_name)

    def print_last_name(self):
        print(self.last_name)

    def print_full_name(self):
        print(self.first_name + ' ' + self.last_name)
'''

class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def name_print(self):
        print(f'Имя: {self.first_name}')

    def last_name_print(self):
        print(f'Фамилия: {self.last_name}')

    def print_full_name(self):
        print(f'Имя и фамилия: {self.first_name + ' ' + self.last_name}')