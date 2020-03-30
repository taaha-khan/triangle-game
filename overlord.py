import turtle
import random
import time

a = turtle.Screen()
a.title('Overlord')
width = 1200; height = width * 0.6
a.setup(width, height)
a.bgcolor('#CDCDCD')
a.tracer(0)

c = a.getcanvas()

all = []
playerSpeed = 5

class Overlord:
    def __init__(self):
        self.drones = []
        self.droneSpeed = 0.5
        self.droneDamage = 10
        self.droneAmount = 8
        self.droneSpread = 20
    
        self.body = turtle.Turtle()
        self.body.shape('circle')
        self.body.color('blue')
        self.body.speed(0)
        self.body.pu()
    
    def initialize_drones(self):
        for _ in range(self.droneAmount):
            d = turtle.Turtle()
            d.speed(0)
            d.dir = (random.randint(-self.droneSpread, self.droneSpread), 
                random.randint(-self.droneSpread, self.droneSpread))
            d.color('black', self.body.pencolor())
            d.pu()
            d.shape('triangle')
            self.drones.append(d)
            all.append(d)


b = Overlord()
b.initialize_drones()

shift = False

def start_shift():
    global shift
    shift = True
    
def end_shift():
    global shift
    shift = False
    

def motion():
    # x, y = event.x, event.y
    x, y = c.winfo_pointerx(), c.winfo_pointery()
    offset = 170
    mousePosition = ((x - (width/2) - offset + 10, (height/2) - y + offset))
    if shift == False:
        b.body.setheading(b.body.towards(mousePosition))
        for dr in b.drones:
            direction = mousePosition[0] + dr.dir[0], mousePosition[1] + dr.dir[1]
            dr.setheading(dr.towards(direction))
            dr.forward(b.droneSpeed)   
    else:
        for d in b.drones:
            direction = mousePosition[0] + d.dir[0], mousePosition[1] + d.dir[1]
            d.setheading(d.towards(direction))
            d.right(180)
            d.forward(b.droneSpeed)

def u():
    for a in all: a.sety(a.ycor() - playerSpeed)
def d():
    for a in all: a.sety(a.ycor() + playerSpeed)
def l():
    for a in all: a.setx(a.xcor() + playerSpeed)
def r():
    for a in all: a.setx(a.xcor() - playerSpeed)



a.listen()
a.onkeypress(u, 'Up')
a.onkeypress(d, 'Down')
a.onkeypress(l, 'Left')
a.onkeypress(r, 'Right')
a.onkeypress(start_shift, 'f')
a.onkeyrelease(end_shift, 'f')
# a._onrelease(end_shift, 2)

# c.bind('<Motion>', motion)

while True:
    motion()
    a.update()


a.mainloop()