class Rob_Peterson:

    name = 'Rob Peterson'
    age = 51
    IsFired = False

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am {self.name}. My age is {self.age}")
    
    def work(self):
        print("I am pretty old, so I am not as creative as I used to be. Doing my best.")


# Bob_Robins.info(Bob_Robins)

class Lion_Johnson:

    name = "Lion El'Jonson"
    age = '>100'
    IsFired = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am {self.name}. My age is {self.age}")
    
    def work(self):
        print("I am not currently available. Sorry for troubles")