#Sawyer Wood, Classes Notes

class subject:
    def __init__(self, content, period, teacher, room):
        self.content = content
        self.period = period
        self.teacher = teacher
        self.room = room

def __str__(self):
    return f"Name: {self.content}\nPeriod: {self.period}\nTeacher: {self.teacher}\nRoom: {self.room}"

first = subject("CS Principles", 1, "LaRose", 200)
second = subject("CP2", 2, "LaRose", 200)

class pokemon:
    def __init__(self, name, species, hp, dmg):
        self.name = name
        self.species = species
        self.hp = hp
        self.dmg = dmg
    
    def __str__(self):
        return f"{self.name} is a {self.species} they hame {self.hp} HP and do {self.dmg} amount of damage in battle."

    def battle(self, opponent):
        while self.hp > 0 and opponent.hp > 0:
            opponent.hp -= self.dmg
            print(f"{self.name} attacked {opponent.name} for {self.dmg} damage and {opponent.name} now has {opponent.hp}.")

            if opponent.hp <= 0:
                print(f"{opponent.name} has been knocked out. {self.name} wins!")
            else:
                self.hp -= opponent.dmg
                print(f"{opponent.name} attacked {self.name} for {opponent.dmg} damage and {self.name} now has {self.hp}.")

                if self.hp <= 0:
                    print(f"{self.name} has been knocked out. {opponent.name} wins!")

fluffy = pokemon("Fluffy", "Arcanine", 280, 110)
slimy = pokemon("Slimy", "Ditto", 100, 70)
spikie = pokemon("Spikie", "Jolteon", 150, 100)

fluffy.battle(spikie)

#Does not work
slimy.battle(spikie)

#What is a class in python?
    #It is a blueprint for an object.

#What is an object in python?
    #It is an instance of a class. 

#How do python classes relate to python objects?
    #Classes are blueprints for creating python objects and other.

#How do you create a python class?
    #You use class and then the name of the class.

#What are methods?
    #Methods are functions that exist in a specific class.

#How do you create a python object?
    #You have object = class()

#How do you call a method for an object?
    #You use object.method()

#Why do we use python classes?
    #We use them to create objects that have specific attributes and methods.