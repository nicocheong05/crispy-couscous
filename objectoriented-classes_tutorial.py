class Character:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.attack = 0
        self.defence = 0
        self.health = 100
        self.experience = 0

    def print_basics(self):
        print("\nName:", self.name)
        print("Age:", self.age)
        print("Attack:", self.attack)
        print("Defence:", self.defence)
        print("Health:", self.health)
        print("Experience:", self.experience)

Nico = Character()
Nico.name = "Nico"
Nico.experience = 3000

Nico.print_basics()

class wizard(Character):
    def __init__(self):
        Character.__init__(self)  #to inherit (or pull) everything from the Character class
        self.magic = 0

    def print_me(self):
        self.print_basics()
        print("Magic:", self.magic)

Merlin = wizard()
Merlin.name = "Merlin"
Merlin.magic = 100
Merlin.experience = 99
Merlin.health = 20
Merlin.print_me()

import random
Knight_rankings =["Grand Master","Master","Seneschal","Marshal","Standard Bearer","Knight","Squire"]

class knight(Character):
    def __init__(self):
        Character.__init__(self)
        self.rank = ""

    def setter(self,name):
        self.name = name
        self.age = random.randint(18,50)
        self.attack = random.randint(0,101)
        self.defence = random.randint(0,101)
        self.health = random.randint(0,101)
        self.experience = random.randint(0,100)
        self.rank = random.choice(Knight_rankings)

    def print_me(self):  #polymorphism is when you can have the same instruction but different outcomes depending on what you are looking for
        self.print_basics()
        print("Rank:", self.rank)

    class weapon:
        def attack():
            print("He swishes his sword")

Bob = knight()
Bob.name = "Bob"
Bob.rank = "Knight"
Bob.attack = 80
Defence = 50
Bob.print_me()
Bob.weapon.attack()

Arthur = knight()
Arthur.setter("Arthur")
Arthur.print_me()
