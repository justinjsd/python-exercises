# Write your solution here:

class Person:
    def __init__(self, name: str):
        self.name = name

    def split_name(self):
        full_name = self.name.split(" ")
        return full_name

    def return_first_name(self):
        return self.split_name()[0]

    def return_last_name(self):
        return self.split_name()[1]

    
if __name__ == "__main__":
    peter = Person("Peter Pythons")
    print(peter.return_first_name())
    print(peter.return_last_name())

    paula = Person("Paula Pythonnen")
    print(paula.return_first_name())
    print(paula.return_last_name())