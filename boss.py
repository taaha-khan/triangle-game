import turtle
import random

s = turtle.Screen()
s.register_shape('boss', ((0, 200), (50, 150), (150, 150) ,(150, 50), (200, 0), (150, -50), (150, -150), (50, -150), (0, -200), (-50, -150), (-150, -150), (-150, -50), (-200, 0), (-150, 50), (-150, 150), (-50, 150)))

class Boss:
    def __init__(self, player, all, enemies, pos):
        self.healthRemaining = 200
        self.damage = 40
        self.missiles = []
        self.missileSpeed = 2
        self.player = player
        self.missileRate = 50
        self.enemies = enemies
        self.all = all

        self.body = turtle.Turtle()
        self.body.speed(0)
        self.body.pu()
        self.body.goto(pos)
        self.body.shape('boss')
        self.body.width(10)
        self.body.color('black','#F6290C')
        self.all.append(self.body)

        self.healthbar = turtle.Turtle()
        self.healthbar.speed(0)
        self.healthbar.pu()
        self.healthbar.color('grey')
        self.healthbar.goto(self.body.xcor(), self.body.ycor() - 250)
        self.healthbar.shape('bar')
        self.healthbar.right(90)
        self.all.append(self.healthbar)

        self.health = turtle.Turtle()
        self.health.speed(0)
        self.health.pu()
        self.health.color('green')
        self.health.left(90)
        self.health.goto(self.healthbar.xcor() - 100, self.healthbar.ycor())
        self.health.shape('boss slider')
        self.all.append(self.health)

    def move(self):
        self.body.right(0.1)
        self.healthbar.goto(self.body.xcor(), self.body.ycor() - 250)
        self.health.goto(self.healthbar.xcor() - 100, self.healthbar.ycor())

    def shoot_missile(self):
        self.missile = turtle.Turtle()
        self.missile.speed(0)
        self.missile.pu()
        self.missile.shape('triangle')
        self.missile.color('orange')
        self.missile.type = 'missile'
        self.missile.dir = random.randint(0, 5)
        self.missile.health = 4
        self.missile.goto(self.body.pos())
        self.missiles.append(self.missile)
        self.all.append(self.missile)
        self.enemies.append(self.missile)