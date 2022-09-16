# This includes constructors.
# My own interpretation.

class Person:
    def __init__(self, name):
        self.name = name

    def talk(name = input("Your name: ")):
        print(f"Hello there {name}!! ")


Person.talk()


# Actual syntax

class Person2:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}. ")


john = Person2("John Smith")
john.talk()