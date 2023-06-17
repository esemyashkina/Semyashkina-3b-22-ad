import os


class TodoList:
    def __init__(self, filename):
        self.filename = filename

    def add_item(self, item):
        if os.path.isfile(self.filename):
            with open(self.filename, 'r') as file:
                items = file.read().splitlines()
        else:
            items = []

        items.append(item)

        with open(self.filename, 'w') as file:
            for item in items:
                file.write(item + '\n')

    def remove_item(self, item):
        if os.path.isfile(self.filename):
            with open(self.filename, 'r') as file:
                items = file.read().splitlines()
        else:
            items = []

        if item in items:
            items.remove(item)

        with open(self.filename, 'w') as file:
            for item in items:
                file.write(item + '\n')

    def display_items(self):
        if os.path.isfile(self.filename):
            with open(self.filename, 'r') as file:
                items = file.read().splitlines()
        else:
            items = []

        if items:
            print("Список домашних дел:")
            for item in items:
                print(item)
        else:
            print("Список домашних дел пуст.")
