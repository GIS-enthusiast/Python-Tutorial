class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        # super().__init__(email)
        User.__init__(self, email)
        self.name = name
        self.power = power
        #self.email = email

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
        Wizard.__init__(self, name, power, email)
        Archer.__init__(self, name, num_arrows)
        #User.__init__(self, email)


hybridborg1 = HybridBorg('Borg', 1000, 90000, 'hybrid@gmail.com')

print(hybridborg1.email)
