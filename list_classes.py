import os
import random

class Monster:
    def __init__(self,id,Name,Origin,Description,Attack,Magical_Force,Magical_Defence,Defence, Intelligence,Health):
        self.id = id
        self.Name = Name
        self.Origin = Origin
        self.Description = Description
        self.Attack = Attack
        self.Magical_Force = Magical_Force
        self.Magical_Defence = Magical_Defence
        self.Defence = Defence
        self.Intelligence = Intelligence
        self.Health = Health

    def __repr__(self):
        return self.Name

    def print_me(self):
        print(self.id,self.Name,self.Origin,self.Description,self.Attack,self.Magical_Force,self.Magical_Defence,self.Defence,self.Intelligence,self.Health)

monster_collection = []

monster_collection.append(Monster(1,"Bog Monster","The bogs of Lincolnshire","A foul monster that sucks people down into the bog!",75,12,15,65,12,99))

def read_monsters():
        try:
            with open('Monsters.txt') as f:
                for line in f:
                    line = line.rstrip()
                    parts = line.split(",")
                    id = parts[0]
                    Name = parts[1]
                    Origin = parts[2]
                    Description = parts[3]
                    Attack = parts[4]
                    Magical_Force = parts[5]
                    Magical_Defence = parts[6]
                    Defence = parts[7]
                    Intelligence = parts[8]
                    Health = parts[9]
                    monster_collection.append(Monster(id,Name,Origin,Description,Attack,Magical_Force,Magical_Defence,Defence,Intelligence,Health))
                    # You code this part
        except OSError:
            print("Sorry, could not find the file. Make sure it is in the correct directory. The current directory is",os.getcwd())

read_monsters()
#number = random.randint(0,len(monster_collection))
print(monster_collection)
