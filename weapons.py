import turtle
import random

run = 0
t = turtle.Turtle()
bullets = []
lastShot = 0
all = []

# Main weapons class
class weapon:
    def __init__(self, Type, speed, spread, reload, shape, damage):
        self.type = Type
        self.speed = speed
        self.spread = spread
        self.reload = reload
        self.shape = shape
        self.damage = damage

    def shoot(self, x, y):
        global run, lastShot
        if run - lastShot >= self.reload:
            lastShot = int(run)
            self.bullet = turtle.Turtle()
            self.bullet.speed(0)
            self.bullet.color('blue')
            self.bullet.pu()
            self.bullet.setheading(t.heading())
            self.bullet.damage = self.damage
            self.bullet.goto(t.pos())
            self.bullet.shape(self.shape)
            self.bullet.right(random.randint(-self.spread, self.spread))
            bullets.append(self.bullet)
            all.append(self.bullet)
