"""
 __ __ __ __ __ __ __ __ __ __ __ __ __ __ __
|                                            |
|   © Taaha Khan 2020                        |
|   All Rights Reserved                      |
|   "Triangle Game" - V 1.1.0                |
|   This is a game about a small tank        |
|   traveling through a map with enemies.    |
|   Inspiration: Diep.io                     |
|   Language: Python Turtle GUI              |
|__ __ __ __ __ __ __ __ __ __ __ __ __ __ __|

"""

# Importing important imports
import turtle
import random
import time

# File Imports
from menu import startMenu
from boss import Boss

# Main measurements
ratio = 0.6
ARENA_WIDTH = 3000
ARENA_HEIGHT = ARENA_WIDTH * ratio
run = 0

all = []

# Window setup
wn = turtle.Screen()
wn.title('Triangle Game')
wn.bgcolor('#CDCDCD')
wn.tracer(0)
# FullScreen = 1442, 980
width = 1200; height = width * 0.6
wn.setup(width, height)

width = wn.window_width()
height = wn.window_height()

mnwidth = int(width); mnheight = int(height)

# Registering shapes
wn.register_shape('side boundary', ((5, ARENA_HEIGHT/2), (-5, ARENA_HEIGHT/2), (-5, -ARENA_HEIGHT/2), (5, -ARENA_HEIGHT/2)))
wn.register_shape('top boundary', ((5, ARENA_WIDTH/2), (-5, ARENA_WIDTH/2), (-5, -ARENA_WIDTH/2), (5, -ARENA_WIDTH/2) ))
wn.register_shape('bar', ((-100, 10), (100, 10), (100, -10), (-100, -10)))
wn.register_shape('slider', ((0, 10), (200, 10), (200, -10), (0, -10)))
wn.register_shape('boss slider', ((0, 10), (200, 10), (200, -10), (0, -10)))
wn.register_shape('heart.gif'); wn.register_shape('clock.gif')
wn.register_shape('target.gif'); wn.register_shape('small circle.gif')
wn.register_shape('bullet', ((-4, -4), (4, -4), (0, 5)))
wn.register_shape('bullet icon', ((-6, -6), (6, -6), (0, 10)))
wn.register_shape('basic', ((-5, 0), (5, 0), (5, 17), (-5, 17), (-5, 0)))
wn.register_shape('closer', ((-5, 0), (5, 0), (5, 15), (-5, 15), (-5, 0)))
wn.register_shape('sniper', ((-5, 0), (5, 0), (5, 22), (-5, 22), (-5, 0)))
wn.register_shape('machine', ((-5, 0), (5, 0), (8, 17), (-8, 17), (-5, 0)))
wn.register_shape('boom', ((-10, 0), (10, 0), (10, 15), (-10, 15), (-10, 0)))
wn.register_shape('twin', ((10, 0), (10, 17), (1, 17), (1, 2), (-1, 2), (-1, 17), (-10, 17), (-10, 0)))
wn.register_shape('shotgun', ((-5, 0), (-5, 17), (-3, 17), (-3, 20), (3, 20), (3, 17), (5, 17), (5, 0)))
wn.register_shape('shield', ((-30, 20), (-10, 30), (10, 30), (30, 20)))
wn.register_shape('shield 2', ((-30, 20), (-10, 30), (10, 30), (30, 20), (30, 15), (10, 25), (-10, 25), (-30, 15)))
wn.register_shape('boss', ((0, 200), (50, 150), (150, 150), (150, 50), (200, 0), (150, -50), (150, -150), (50, -150), (0, -200), (-50, -150), (-150, -150), (-150, -50), (-200, 0), (-150, 50), (-150, 150), (-50, 150)))

canvas = wn.getcanvas()

# Arena boundaries
leftWall = turtle.Turtle()
leftWall.speed(0)
leftWall.shape('side boundary')
leftWall.left(90)
leftWall.pu()
leftWall.setx(-ARENA_WIDTH/2)
leftWall.mainPos = leftWall.pos()
all.append(leftWall)

rightWall = leftWall.clone()
rightWall.setx(ARENA_WIDTH/2)
rightWall.mainPos = rightWall.pos()
all.append(rightWall)

topWall = turtle.Turtle()
topWall.speed(0)
topWall.shape('top boundary')
topWall.pu()
topWall.sety(ARENA_HEIGHT/2)
topWall.mainPos = topWall.pos()
all.append(topWall)

bottomWall = topWall.clone()
bottomWall.sety(-ARENA_HEIGHT/2)
bottomWall.mainPos = bottomWall.pos()
all.append(bottomWall)

walls = []
walls.append(topWall)
walls.append(bottomWall)
walls.append(leftWall)
walls.append(rightWall)

# Scoring
hits = 0


scorer = turtle.Turtle()
scorer.speed(0)
scorer.ht()
scorer.pu()
scorer.goto(0, -height/2 + 70)
scorer.color('black')
scorer.write('Basic Tank', move=False, align="center", font=("Open Sans", 18, "bold"))

# Minimap setup
if ratio == 1: mapWidth = 300
else: mapWidth = 350
mapHeight = mapWidth * ratio

scl = ARENA_WIDTH/(mapWidth/2)

mmap = turtle.Turtle()
mmap.width(4)
mmap.speed(0)
mmap.ht()
mmap.pu()
mmap.goto(-width/2 + 20, height/2 - 20)
mmap.pd()
mmap.setx(mmap.xcor() + mapWidth/2)
mmap.sety(mmap.ycor() - mapHeight/2)
mmap.setx(mmap.xcor() - mapWidth/2)
mmap.sety(mmap.ycor() + mapHeight/2)
mmap.pu()

mini = turtle.Turtle()
mini.speed(0)
mini.color('blue')
mini.pu()
mini.setposition( -width/2 + 20 + mapWidth/4, height/2 - 20 - mapHeight/4 )
mini.ht()
mini.dot(5)

# Stats Counter

i = turtle.Turtle()
i.speed(0)
i.width(3)
i.pu()
i.ht()
i.shape('triangle')
i.color('red')
i.left(90)
i.goto(width/2 - 180, height/2 - 38)
i.stamp()

i.goto(width/2 - 255, height/2 - 36)
i.shape('clock.gif')
i.stamp()

i.pu()
i.shape('bullet icon')
i.color('blue')
i.goto(width/2 - 70, height/2 - 35)
i.stamp()

i.pu()
i.goto(width/2 - 120, height/2 - 32)
i.shape('heart.gif')
i.st()


w = mini.clone()
w.color('black')
w.goto(width/2 - 235, height/2 - 45)



# Main Player ==========================================

# Variables
auto = False
auto_spin = False
playerSpeed = 5
enemyCount = 15
enemySpeed = 1.5
enemyRespawn = 5
lastShot = 0
miniSpeed = playerSpeed / scl
miniUnit = miniSpeed / playerSpeed

# shield = turtle.Turtle()
# shield.speed(0)
# shield.shape('shield 2')
# shield.pu()
# shield.color('#535353')

# Gun
gun = turtle.Turtle()
gun.speed(0)
gun.shape('basic')
gun.color('#555555','grey')
gun.goto(0, 0)

t = turtle.Turtle()
t.speed(0)
t.penup()
t.color('blue')
t.health = 200
t.shape('circle')

mouse = turtle.Turtle()
mouse.speed(0)
mouse.pu()
mouse.shape('target.gif')

# Facing mouse pointer
x, y = canvas.winfo_pointerx(), canvas.winfo_pointery()
def motion(event):
    global auto_spin
    x, y = event.x, event.y
    mousePosition = (x - (width)/2, -y + (height)/2 )
    mouse.setpos(mousePosition)
    if not auto_spin:
        t.setheading(t.towards(mouse))
        gun.setheading(t.heading())
    # shield.seth(t.heading())
canvas.bind('<Motion>', motion)

# Health bar
healthBar = turtle.Turtle()
healthBar.speed(0)
healthBar.pu()
healthBar.goto(0, (-height/2) + 50)
healthBar.shape('bar')
healthBar.right(90)
healthBar.color('grey')
healthBar.stamp()

health = healthBar
health.shape('slider')
health.right(180)
health.goto(-100, (-height/2) + 50)
health.color('green')

# ======================================================

# Main weapons class
bullets = []
class weapon:
    def __init__(self, Type, speed, spread, reload, shape, damage, recoil, amount):
        self.type = Type
        self.speed = speed
        self.spread = spread
        self.reload = reload
        self.shape = shape
        self.damage = damage
        self.recoil = recoil
        self.amount = amount

    def shoot(self, x, y):
        global run, lastShot
        if run - lastShot >= self.reload:
            lastShot = int(run)
            for i in range(self.amount):
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
                if self.type == 'Twin':
                    if i == 1: 
                        self.bullet.right(90)
                        self.bullet.fd(10)
                        self.bullet.left(90)
                    elif i == 2: 
                        self.bullet.left(90)
                        self.bullet.fd(10)
                        self.bullet.right(90)
                elif self.type == 'Shotgun':
                    if i == 1: self.bullet.forward(self.speed * 5)
            # Recoil
            leftWall.origin = leftWall.pos(); rightWall.origin = rightWall.pos()
            bottomWall.origin = bottomWall.pos(); topWall.origin = topWall.pos()
            for w in walls:
                w.original = w.heading()
                w.seth(t.heading())
                w.forward(self.recoil)
            if topWall.ycor() - playerSpeed > t.ycor() + 10 and bottomWall.ycor() + playerSpeed < t.ycor() - 10 and rightWall.xcor() - playerSpeed > t.xcor() + 10 and leftWall.xcor() + playerSpeed < t.xcor() - 10:
                for w in walls: w.goto(w.origin); w.seth(w.original)
                for a in all:
                    a.original = a.heading()
                    a.seth(t.heading())
                    a.forward(self.recoil)
                    a.seth(a.original)
                mini.seth(t.heading())
                mini.clear()
                mini.backward(self.recoil * miniUnit)
                mini.dot(5)
            else: 
                for w in walls: w.goto(w.origin); w.seth(w.original)


# Resetting position offscreen
def away():
    global width
    position = (random.randint(int(leftWall.xcor() + 100), int(rightWall.xcor() - 100)), random.randint(int(bottomWall.ycor() + 100), int(topWall.ycor() - 100)))
    while t.distance(position) <= width/2: 
        position = (random.randint(int(leftWall.xcor() + 100), int(rightWall.xcor() - 100)), random.randint(int(bottomWall.ycor() + 100), int(topWall.ycor() - 100)))
    return position

# Health regen heart
heart = turtle.Turtle()
heart.speed(0)
heart.shape('heart.gif')
heart.pu()
heart.setposition(away())
hearts = 0
all.append(heart)


def miniHeartPos():
    xoff = heart.xcor() - leftWall.xcor()
    yoff = heart.ycor() - topWall.ycor()
    miniHeartX = (-mnwidth/2 + 20) + (xoff * miniUnit)
    miniHeartY = (mnheight/2 - 20) + (yoff * miniUnit)
    return miniHeartX, miniHeartY

def miniPlayerPos():
    xoff = t.xcor() - leftWall.xcor()
    yoff = t.ycor() - topWall.ycor()
    miniPlayerX = (-mnwidth/2 + 20) + (xoff * miniUnit)
    miniPlayerY = (mnheight/2 - 20) + (yoff * miniUnit)
    return miniPlayerX, miniPlayerY

miniHeart = mini.clone()
miniHeart.clear()
miniHeart.color('red')
miniHeart.goto(miniHeartPos())
miniHeart.dot(5)


# Generating enemies
enemies = []
def generate_enemies():
    e = turtle.Turtle()
    e.speed(0)
    e.penup()
    e.health = 3
    e.shape('triangle')
    e.color('red')
    e.setposition(away())
    e.type = 'basic'
    e.setheading(e.towards(t))
    enemies.append(e)
    all.append(e)
    return e

def generate_guardian(angle):
    g = turtle.Turtle()
    g.speed(0)
    g.penup()
    g.shape('triangle')
    g.color('black')
    g.health = 10
    g.setheading(angle)
    if angle == 0: g.setposition(heart.xcor(), heart.ycor() - 50)
    elif angle == 90: g.setposition(heart.xcor() + 50, heart.ycor())
    elif angle == 180: g.setposition(heart.xcor(), heart.ycor() + 50)
    elif angle == 270: g.setposition(heart.xcor() - 50, heart.ycor())
    g.origin = g.pos()
    g.angle = g.heading()
    g.home = True
    g.type = 'guardian'
    enemies.append(g)
    all.append(g)
    return g


angle = 0
for i in range(4): 
    generate_guardian(angle)
    angle += 90
for i in range(enemyCount): generate_enemies()
for e in enemies:
    if e not in all: all.append(e)



# bos = Boss()

# Autoshooting
def autoShoot():
    global auto, run
    if auto == False: 
        auto = True; wn.onscreenclick(None)
        alert('Auto Fire: ON')
        al.lastRun = int(run)
    else: 
        auto = False; wn.onscreenclick(t.weapon.shoot)
        alert('Auto Fire: OFF')
        al.lastRun = int(run)

# Auto Spinning
def autoSpin():
    global auto_spin, run
    if auto_spin == False: 
        auto_spin = True
        alert('Auto Spin: ON')
        al.lastRun = int(run)
    elif auto_spin == True: 
        auto_spin = False
        alert('Auto Spin: OFF')
        al.lastRun = int(run)

# Setting weapons

t.weapon = None

def updateScore():
    scorer.clear()
    scorer.write(str(t.weapon.type), move=False, align="center", font=("Open Sans", 18, "bold"))

def sniper():
    gun.shape('sniper')
    t.weapon = weapon(Type = 'Sniper', speed = 8, spread = 0, reload = 30, shape = 'bullet', damage = 4, recoil = 1, amount = 1)
    updateScore()    
def machine_gun():
    gun.shape('machine')
    t.weapon = weapon(Type = 'Machine Gun', speed = 4, spread = 10, reload = 7, shape = 'bullet', damage = 1.5, recoil = 3, amount = 1)
    updateScore()
def basic():
    gun.shape('basic')
    t.weapon = weapon(Type = 'Basic Tank', speed = 6, spread = 4, reload = 20, shape = 'bullet', damage = 1.5, recoil = 1, amount = 1)
    updateScore()
def boomer():
    gun.shape('boom')
    t.weapon = weapon(Type = 'Boomer', speed = 3, spread = 0, reload = 100, shape = 'circle', damage = 5, recoil = 50, amount = 1)
    updateScore()
def arena_closer():
    gun.shape('closer')
    t.weapon = weapon(Type = 'Arena Closer', speed = 10, spread = 0, reload = 9, shape = 'small circle.gif', damage = 6, recoil = 3, amount = 1)
    updateScore()
def twin():
    gun.shape('twin')
    t.weapon = weapon(Type = 'Twin', speed = 4, spread = 2, reload = 10, shape = 'bullet', damage = 1.5, recoil = 3, amount = 2)
    updateScore()
def shotgun():
    gun.shape('shotgun')
    t.weapon = weapon(Type = 'Shotgun', speed = 8, spread = 2, reload = 20, shape = 'bullet', damage = 3, recoil = 2, amount = 2)
    updateScore()

basic()

# Movement functions
def up():
    if topWall.ycor() - playerSpeed > t.ycor() + 10:
        for a in all: a.sety(a.ycor() - (playerSpeed))
        mini.clear()
        mini.sety(mini.ycor() + miniSpeed)
        mini.dot(5)
def down():
    if bottomWall.ycor() + playerSpeed < t.ycor() - 10:
        for a in all: a.sety(a.ycor() + (playerSpeed))
        mini.clear()
        mini.sety(mini.ycor() - miniSpeed)
        mini.dot(5)
def right():
    if rightWall.xcor() - playerSpeed > t.xcor() + 10:
        for a in all: a.setx(a.xcor() - (playerSpeed))
        mini.clear()
        mini.setx(mini.xcor() + miniSpeed)
        mini.dot(5)
def left():
    if leftWall.xcor() + playerSpeed < t.xcor() - 10:
        for a in all: a.setx(a.xcor() + (playerSpeed))
        mini.clear()
        mini.setx(mini.xcor() - miniSpeed)
        mini.dot(5)



wn.listen()

# Movement
def movement():
    wn.onkeypress(up, 'w')
    wn.onkeypress(down, 's')
    wn.onkeypress(left, 'a')
    wn.onkeypress(right, 'd')

    wn.onkeypress(up, 'Up')
    wn.onkeypress(down, 'Down')
    wn.onkeypress(left, 'Left')
    wn.onkeypress(right, 'Right')

# Pausing Movement
def stopMovement():
    wn.onkeypress(None, 'w')
    wn.onkeypress(None, 's')
    wn.onkeypress(None, 'a')
    wn.onkeypress(None, 'd')

    wn.onkeypress(None, 'Up')
    wn.onkeypress(None, 'Down')
    wn.onkeypress(None, 'Left')
    wn.onkeypress(None, 'Right')

movement()


# Shooting

wn.onscreenclick(t.weapon.shoot)
wn.onkey(autoShoot, 'e')
wn.onkey(autoSpin, 'c')

wn.onkey(basic, '1')
wn.onkey(sniper, '2')
wn.onkey(machine_gun, '3')
wn.onkey(boomer, '4')
wn.onkey(twin, '5')
wn.onkey(shotgun, '6')
wn.onkey(arena_closer, 'f')


# AI Algorithm
enemiesAI = []
enemiesAI = enemies[:]

def AI():
    global enemiesAI, enemySpeed, enemyRespawn
    enemyRespawn = 5
    if run % 100 == 0: enemiesAI = enemies[:]
    if len(enemiesAI) > 1:
        least = 10000
        closest = None
        for e in enemiesAI:
            if e.distance(t) < least:
                least = e.distance(t)
                closest = e
        enemiesAI.remove(closest)
        sniper()
        autoShoot()
        t.setheading(t.towards(closest))
        gun.setheading(t.heading())
        t.weapon.shoot(0,0)
    if t.health != 200: tx, ty = heart.xcor(), heart.ycor()
    else: tx, ty = heart.xcor(), heart.ycor()
    if t.distance(tx, ty) >= 20:
        if abs(ty - t.ycor()) > 10:
            if ty > t.ycor(): up()
            elif ty < t.ycor(): down()
        if abs(tx - t.xcor()) > 10:
            if tx > t.xcor(): right()
            elif tx < t.xcor(): left()
    

# Resetting window size
def window():
    global width, height
    if wn.window_height() != height or wn.window_width() != width:
        width = wn.window_width()
        height = wn.window_height()

def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    mins = mins % 60
    if sec < 10: return f'{int(mins)}:0{int(sec)}'
    return f'{int(mins)}:{int(sec)}'

start = time.time()

replaced = False
filler = []
bossActivated = False


def reset(x, y):
    global replaced, hurt, auto, auto_spin, hits, hearts
    replaced = True
    for w in walls: w.goto(w.mainPos)
    for e in enemies: e.ht()
    enemies.clear()
    for b in bullets: b.ht()
    bullets.clear()
    t.health = 200
    wn.register_shape('slider', ((0, 10), (t.health, 10), (t.health, -10), (0, -10)))
    hurt = False
    auto = False
    auto_spin = False
    health.shape('slider')
    hits = 0
    hearts = 0
    heart.goto(away())
    al.clear()
    angle = 0
    for i in range(4):
        generate_guardian(angle)
        angle += 90
        filler.append(i)
    filler.clear()
    miniHeart.clear()
    miniHeart.goto(miniHeartPos())
    miniHeart.dot(5)
    mini.clear()
    mini.goto(miniPlayerPos())
    mini.dot(5)
    for i in range(enemyCount): generate_enemies()
    return

al = turtle.Turtle()
al.speed(0)
al.lastRun = 0
al.pu(); al.ht()
al.color('blue')

def alert(text):
    al.clear()
    al.color('blue')
    al.pu()
    al.goto(-70, height/2 - 28)
    al.seth(0)
    al.pd()
    al.begin_fill()
    al.forward(130)
    al.right(90)
    al.forward(25)
    al.right(90)
    al.forward(130)
    al.end_fill()
    al.pu()
    al.goto(-4, height/2 - 50)
    al.color('white')
    al.write(str(text), move=False, align="center", font=("Open Sans", 13, "bold"))


# Intialization
run = 0
dead = False
hurt = False
nextRespawn = 100
hitBy = None
boss = None
bossSpawn = 100


# Main Game Loop
while True:
    wn.update()
    
    run += 1


    now = time.time()
    secs = now - start
    timer = time_convert(secs)

    enCount = len(enemies)
    if enCount < 10:
        enCount = '0' + str(enCount)

    w.clear()
    w.write(str(timer) + '          ' + str(enCount) + '            ' + str(hearts) + '        ' + str(hits), move=False, align="left", font=("Open Sans", 12, "bold"))

    if run - al.lastRun > 400:
        al.clear()
    
    # Moving Enemies
    for e in enemies:
        if e.type == 'basic':
            e.setheading(e.towards(t.pos()))
            e.forward(enemySpeed)
        elif e.type == 'missile': 
            dir = e.dir
            if dir == 0: e.seth(e.towards(t.xcor(), t.ycor() + 100))
            elif dir == 1: e.seth(e.towards(t.xcor(), t.ycor() - 100))
            elif dir == 2: e.seth(e.towards(t.xcor() + 100, t.ycor()))
            elif dir == 3: e.seth(e.towards(t.xcor() - 100, t.ycor()))
            elif dir == 4 or dir == 5: e.seth(e.towards(t))
            if bossActivated: e.forward(boss.missileSpeed)
            # if e.distance(dir) < 10: e.dir = 5
        # Guardian Movement
        elif e.type == 'guardian':
            # Circling
            if e.distance(t) > 300 and e.home:
                e.left(0.5)
                e.forward(enemySpeed/2)
                e.home = True
            # Attacking
            elif t.distance(heart) <= 400:
                e.seth(e.towards(t))
                e.forward(enemySpeed * 2)
            elif e.distance(heart) >= 300 and not e.home:
                # Returning Home
                if e.distance(e.origin) >= 5 and t.distance(heart) > 300 and not e.home:
                    e.seth(e.towards(e.origin))
                    e.forward(enemySpeed)
                # Resuming Circling
                elif e.distance(e.origin) <= 5:
                    e.setpos(e.origin)
                    e.seth(e.angle)
                    e.home = True
        # Deducting Damage
        if e.distance(t) <= 20:
            e.ht()
            enemies.remove(e)
            all.remove(e)
            hitBy = e
            hurt = True; break

    # Moving bullets
    if auto and run % t.weapon.reload == 0: t.weapon.shoot(0, 0)
    if auto_spin: t.right(2); gun.right(2)
    for b in bullets:
        b.shape(t.weapon.shape)
        b.forward(t.weapon.speed)
        # Ending at walls and viewscreen
        if b.xcor() < leftWall.xcor() or b.xcor() > rightWall.xcor() or b.ycor() < bottomWall.ycor() or b.ycor() > topWall.ycor():
            try:
                b.ht()
                bullets.remove(b)
                all.remove(b)
            except: ValueError
        # Window penetration
        elif t.weapon.type != 'Sniper' or t.weapon.type != 'Arena Closer':
            if b.xcor() > width/2 + 50 or b.xcor() < -width/2 - 50 or b.ycor() > height/2 + 50 or b.ycor() < -height/2 - 50:
                try:
                    b.ht(); bullets.remove(b)
                    all.remove(b)
                except: ValueError
        # Hitting enemies
        for e in enemies:
            if b.distance(e) <= 20:
                e.health -= b.damage
                if t.weapon.type != 'Boomer' and t.weapon.type != 'Arena Closer':
                    b.damage -= e.health + b.damage/2
                    if b.damage <= 0:
                        try: 
                            bullets.remove(b); b.ht() 
                            all.remove(b)  
                        except: ValueError
                # Deleting Enemies
                if e.health <= 0:
                    # Penetrating through enemies
                    e.ht(); enemies.remove(e)
                    all.remove(e)
                    # Setting score
                    hits += 1
        
        if bossActivated:
            boss.body.color('black','#F6290C')
            if b.distance(boss.body) <= 180:
                b.ht()
                try: bullets.remove(b)
                except: ValueError
                boss.healthRemaining -= t.weapon.damage
                wn.register_shape('boss slider', ((0, 10), (boss.healthRemaining, 10), (boss.healthRemaining, -10), (0, -10)))
                boss.health.shape('boss slider')
                boss.body.color('black','orange')
                wn.update()
            if boss.healthRemaining <= 0:
                alert('Boss Defeated')
                al.lastRun = int(run)
                boss.body.goto(width * 1000, height * 1000)
                boss.health.goto(width * 1000, height * 1000)
                boss.healthbar.goto(width * 1000, height * 1000)
                boss.body.ht()
                bossActivated = False
                hits += 50
                bossSpawn += run

    # If hit by enemy
    if hurt:
        lastHit = int(run)
        if (hitBy.type == 'basic' or hitBy.type == 'missile') and t.health - 20 >= 0: t.health -= 20
        elif hitBy.type == 'guardian' and t.health - 40 > 0: t.health -= 40
        else: t.health = 0
        wn.register_shape('slider', ((0, 10), (t.health, 10), (t.health, -10), (0, -10)))
        hurt = False
        health.shape('slider')
        if t.health <= 0:
            dead = True
    # Health regen
    elif not hurt: 
        if run % 1500 == 0 and t.health + 20 <= 200 and abs(run - lastHit) >= 2000:
            t.health += 20
            wn.register_shape('slider', ((0, 10), (t.health, 10), (t.health, -10), (0, -10)))
            health.shape('slider')
    
    # Heart health regen
    if heart.distance(t) <= 30:
        alert('Heart Gained')
        al.lastRun = int(run)
        if t.health + 40 <= 200:
            t.health += 40
        elif t.health + 20 <= 200:
            t.health += 20
        heart.setposition(away())
        hearts += 1
        wn.register_shape('slider', ((0, 10), (t.health, 10), (t.health, -10), (0, -10)))
        health.shape('slider')
        miniHeart.clear()
        miniHeart.goto(miniHeartPos())
        miniHeart.dot(5)
        for e in enemies:
            if e.type == 'guardian':
                enemies.remove(e)
                e.ht(); all.remove(e)
        angle = 0
        for i in range(4): 
            generate_guardian(angle)
            angle += 90

    # Boss
    if run == bossSpawn:
        boss = Boss(t, all, enemies, away())
        bossActivated = True
        boss.healthRemaining = 200
        wn.register_shape('boss slider', ((0, 10), (boss.healthRemaining, 10), (boss.healthRemaining, -10), (0, -10)))
        boss.health.shape('boss slider')
        alert('Boss Activated')
        al.lastRun = int(run)
    if bossActivated:
        boss.move()
        if run % boss.missileRate == 0 and boss.body.distance(t) <= width/2 + 180:
            boss.shoot_missile()
        if t.distance(boss.body) <= 180:
            dead = True

    
    # GameLoop Reset
    if dead:
        t.health = 0
        wn.register_shape('slider', ((0, 10), (t.health, 10), (t.health, -10), (0, -10)))
        health.shape('slider')
        health.color('red')
        scoreFile = open('highScore.txt', 'w+')
        scoreFile.write(f"\nHits: {hits},  Hearts: {hearts},  Time Alive: {time.time() - start} secs")
        scoreFile.close()
        while not replaced:
            stopMovement()
            wn.onscreenclick(reset)
            wn.bgcolor('#98999B')
            wn.update()
            scorer.clear()
            scorer.write('Click Anywhere to Restart', move=False, align="center", font=("Open Sans", 18, "bold"))
        if replaced: 
            wn.bgcolor('#CDCDCD')
            start = time.time()
            movement()
            basic()
            t.health = 200
            wn.register_shape('slider', ((0, 10), (t.health, 10), (t.health, -10), (0, -10)))
            health.shape('slider')
            health.color('green')
            dead = False
            run = 0
            if bossActivated: boss.body.goto(away()); boss.move(); boss.body.st()
            else: boss.body.goto(10000,1000000); boss.body.ht()
            wn.listen()
        wn.onscreenclick(t.weapon.shoot)
        replaced = False

    # Respawning enemies
    r = random.randint(0, int(len(enemies) * enemyRespawn / 2))
    # r = 10000
    if r == 0: 
        newEnemy = generate_enemies()
        enemiesAI.append(newEnemy)
    
    # Speed enemy respawn
    if hits > nextRespawn:
        nextRespawn += 100
        if enemyRespawn - 1 > 1: enemyRespawn -= 1
        elif run % nextRespawn/2 == 0: generate_enemies()
        enemySpeed += 0.5

    # Window Size
    window()

# Ending Program
wn.exitonclick()
