from tkinter import *
import random
import math

const_INITIAL_PEOPLE = 4
const_INITIAL_FAMILIES=2
const_HOUSES = 5
const_DAY_LENGTH = 5000
const_MOVEMENT_SPEED = 10

class Location():
    id = 0
    const_X = 0
    const_Y = 0
    const_RADIUS = 0
    name=""
    color=""

    def __init__(self, x,y,rad,name, color, id):
        self.const_X = x
        self.const_Y = y
        self.const_RADIUS = rad
        self.name = name
        self.color = color
        self.id = id
    def getRadius(self):
        return self.const_RADIUS
    def getX(self):
        return self.const_X
    def getY(self):
        return self.const_Y

class Person:
    x=0
    y=0
    name=""
    emotion = 0 #0 happy, 1 unhappy, 2 stressed
    health = 100
    educated = False
    canWork = True
    age = 0

    houseid = 0
    workid = 0
    familyid = 0
    id=0

    destinationx=0
    destinationy=0

    maxHealth = 100

    const_AGE_LENGTH = 100

    def __init__(self, name,id):
        self.name = name
        self.id=id
        print(self.name + " is looking for a house")
        done = False
        for p in places:
            if(done):
                break
            if("House" in p.name):
                for pe in people:
                    if (pe.houseid != p.id or pe.familyid == self.familyid):
                        if(pe.houseid != p.id):
                            print("House unoccupied")
                        elif(pe.familyid != self.familyid):
                            print("House is occupied by family")
                        self.houseid = p.id
                        print("Assigning house " + str(p.id))
                        self.x=p.getX()
                        self.y=p.getY()

                        done=True
                        break

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
            for p in places:
                if p.id == self.houseid:
                    print(str(p.id) + str(self.houseid))
                    self.destinationx = p.getX()
                    self.destinationy = p.getY()
                    print(self.name + " is going to home")
                    return
        elif world.time > 1000 and self.canWork:
            for p in places:
                if p.id == self.workid:
                    self.destinationx = p.getX()
                    self.destinationy = p.getY()
                    print(self.name + " is going to work")
        elif world.time > 1000 and not self.canWork and not self.educated:
            for p in places:
                if p.name == "School":
                    self.destinationx = p.getX()
                    self.destinationy = p.getY()
                    print(self.name + " is going to school")
        else:
            for p in places:
                if p.id == self.houseid:
                    print(str(p.id) + str(self.houseid))
                    print(self.name + " is going to home")
                    self.destinationx = p.getX()
                    self.destinationy = p.getY()

    def update(self):
        if (self.health <= 0):
            self.die()
        self.age += 1
        if(self.age % self.const_AGE_LENGTH  == 0):
            self.maxHealth = 100 - (self.age / self.const_AGE_LENGTH)

        index = 0
        for p in people:
            if (p.id == self.id):
                canvas.tag_raise(peopleIcons[index])
                break
            index+=1
        i=0
        self.findDestination()
        for pi in peopleIcons:
           if(i == index):


                xlocation=int(canvas.coords(pi)[0])
                ylocation=int(canvas.coords(pi)[1])

                dx=self.destinationx
                dy=self.destinationy

                xmove = norm(xlocation - self.destinationx) * const_MOVEMENT_SPEED
                ymove = norm(ylocation - self.destinationy) * const_MOVEMENT_SPEED

                canvas.move(pi, -xmove,-ymove)

                break
           i+=1

def norm(i):
    if(i > 0):
        return 1
    else:
        return -1
    return 0
class World:
    time = 0
def update():
    for p in people:
        p.update()

    world.time += 1
    if(world.time>const_DAY_LENGTH):
        world.time = 0
    canvas.update()
    canvas.update_idletasks()
    root.update()
    root.update_idletasks()
    root.after(1, update)

def getLocationByID(identifier):
    for p in places:
        if(p.id == identifier):
            return p
    return None

people = []
peopleIcons = []
places = []

places.append(Location(50,300, 40, "School", "green", 0))
places.append(Location(900,100, 99, "High Level Workplace", "gray", 1))
places.append(Location(900,300, 99, "Low Level Workplace", "gray", 2))

for i in range(0, const_HOUSES):
    places.append(Location(50+(75 * i), 50, 25,"House " + str(i), "brown", 3+i))

names = open("names.txt", "r").read().split("\n")

root = Tk()

canvas = Canvas(root, width=1000, height=1000)
canvas.pack()

for i in range(0, const_INITIAL_PEOPLE):
    people.append(Person(names[random.randint(0, 49)],i))
    peopleIcons.append(canvas.create_rectangle(0,0,20,20, fill="blue"))
for i in range(0, const_INITIAL_FAMILIES-1):
    people[i].familyid=i

for p in places:
    canvas.create_oval(p.getX() + p.getRadius(), p.getY() + p.getRadius(), p.getX() - p.getRadius(), p.getY() - p.getRadius(), fill=p.color)
world = World()
root.after(500,update)
root.mainloop()