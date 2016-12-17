import random

const_INITIAL_PEOPLE = 4
const_INITIAL_FAMILIES = 2
const_DAY_LENGTH = 5000
class World:
    time = 0
class Family:
    householdWealth = 0
    identifier=0
    def __init__(self, identifier):
        self.identifier=identifier

class Person:
    name=""
    emotion = 0 #0 happy, 1 unhappy, 2 stressed
    health = 100
    education = 0
    canWork = True
    age = 0
    money=0

    id=0

    destination = ""

    maxHealth = 100

    const_AGE_LENGTH = 100

    def __init__(self, name,id):
        self.name = name
        self.id=id

    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def setX(self, newx):
        self.x = newx
    def setY(self, newy):
        self.y = newy
    def changeHealth(self, value):
        self.health += value
        if(self.health > self.maxHealth):
            self.health = self.maxHealth
    def setEmotion(self, value):
        if(value > 2 or value < 0):
            print("Error, emotion above limit")
    def setEducated(self):
        self.educated = True
    def getEducated(self):
        return self.educated
    def getWork(self):
        return self.canWork
    def setWork(self):
        self.canWork = True
    def die(self):
        print(self.name + " has died")

    def findDestination(self):
        if world.time >3000:
                print(self.name + " is going to home")
                self.destination = "H"
                return
        elif world.time > 1000 and self.canWork:
                    print(self.name + " is going to work")
                    self.destination = "W"
        elif world.time > 1000 and not self.canWork and not self.educated:
                    print(self.name + " is going to school")
                    self.destination = "S"
        else:
                    print(self.name + " is going to home")
                    self.destination = "H"

    def update(self):
        if (self.health <= 0):
            self.die()
        self.age += 1
        if(self.age % self.const_AGE_LENGTH  == 0):
            self.maxHealth = 100 - (self.age / self.const_AGE_LENGTH)

        self.findDestination()
        if(self.destination == "S"):
            self.education+=1
            if self.educated>1000:
                self.educated=True
                self.canWork=True
        if(self.age >= 1002):
            self.canWork = True

        if(self.destination == "W"):
            if(self.educated):
                self.money+=2
            else:
                self.money+=1

people = []
world = World()
names = open("names.txt", "r").read().split("\n")
for i in range(0, const_INITIAL_PEOPLE):
    people.append(Person(names[random.randint(0, 49)],i))

for i in range(0, const_INITIAL_FAMILIES):
    

def update():
    for p in people:
        p.update()

    world.time += 1
    if(world.time>const_DAY_LENGTH):
        world.time = 0