#users can be wizards, archers, etc, but they must be signed in first.

class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self): 
        print('logged in')
    

class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        #User.__init__(self, email)
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'attacking with a power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    
    def attack(self):
        print(f'attacking with arrows: arrows left- {self.num_arrows}')

    def run(self):
        print('ran really fast')

class HybridBorg(Wizard, Archer, User):
    def __init__(self, name, power, num_arrows, email):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, num_arrows)
        User.__init__(self, email)
      

#wizard1 = Wizard('Merlin', 60, 'merlin@gmail.com')
#archer1 = Archer('Robin', 30)
hybrid1 = HybridBorg('Borg', 1000, 90000, 'hybrid@gmail.com')

print(hybrid1.email)







'''

class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name #attributes of the objects
        self._age = age # Underscore indicates privacy.

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self._name} and I am {self._age} years old')

player1 = PlayerCharacter('Andrei', 100)

print(player1._age)
'''

