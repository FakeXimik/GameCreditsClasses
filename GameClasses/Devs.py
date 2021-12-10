class Bob_Robins:

    name = 'Bob Robins'
    age = 32
    IsFired = False

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am {self.name}. My age is {self.age}")
    
    def work(self):
        print("I am a cool and productive. Working in progress.")


# Bob_Robins.info(Bob_Robins)

class Jaghatai:

    name = 'Jaghatai Khan'
    age = 'pretty old'
    IsFired = False

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am {self.name}. I am {self.age}")
    
    def work(self):
        print("I'll start working when the lunch ends.")