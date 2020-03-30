import turtle
import random
import time

s = turtle.Screen()
s.tracer(0)
s.title('Triangle Game - Menu')
s.bgcolor('#CDCDCD')

s.register_shape('basic', ((-5, 0), (5, 0), (5, 15), (-5, 15), (-5, 0)))
s.register_shape('heart.gif')

c = s.getcanvas()


width = 1200
height = width * 0.6

s.setup(width, height)

def window():
    global width, height
    if s.window_height() != height or s.window_width() != width:
        width = s.window_width()
        height = s.window_height()


view = []
for i in range(20):
    a = turtle.Turtle()
    a.speed(0)
    a.pu()
    a.color('red')
    a.shape('triangle')
    a.seth(random.randint(0, 360))
    a.goto(random.randint(-width/2, width/2), random.randint(-height/2, height/2))
    view.append(a)




def startMenu():

    global menuWidth
    global menuHeight
    menuWidth = width - 400
    menuHeight = height - 200
    
    b = turtle.Turtle()
    b.speed(0)
    b.pu(); b.ht()
    b.color('#0E1E1E')
    b.goto(-menuWidth/2, menuHeight/2)
    b.pd()
    b.begin_fill()
    b.setx(b.xcor() + menuWidth)
    b.sety(b.ycor() - menuHeight)
    b.setx(b.xcor() - menuWidth)
    b.sety(b.ycor() + menuHeight)
    b.end_fill()

    b.pu()
    b.color('white')
    b.goto(0, menuHeight/2 - 100)
    b.write('< TRIANGLE GAME >', move=False, align="center", font=("Open Sans", 50, "bold"))

    b.goto(-250, 50)
    b.write('PLAY', move=False, align="left", font=("Open Sans", 30, "bold"))
    b.goto(200, 75)
    b.shape('basic')
    b.color('#555555','grey')
    b.left(45)
    b.stamp()
    b.shape('circle')
    b.color('blue')
    b.stamp()

    b.color('white')

    b.goto(-250, -20)
    b.write('OPTIONS', move=False, align="left", font=("Open Sans", 30, "bold"))

    b.goto(-250, -90)
    b.write('EXIT', move=False, align="left", font=("Open Sans", 30, "bold"))
    b.goto(200, -60)
    b.shape('triangle')
    b.color('red')
    b.stamp()

    b.goto(200, 10)
    b.st()
    b.shape('heart.gif')
    b.stamp()

    b.ht()

    return b

        
def click(x, y):
    b.goto(x, y)
    if abs(b.xcor() - -200) <= 40 and abs(b.ycor() - 75) <= 20:
        # Play Game
        clearMenu()
        c.unbind('<Motion>')
        s.onscreenclick(None)
        import game
        game.wn.onscreenclick(game.t.weapon.shoot)
        return False
    elif abs(b.xcor() - -175) <= 90 and abs(b.ycor() - 5) <= 20:
        # Options/Tutorial
        pass
    elif abs(b.xcor() - -200) <= 40 and abs(b.ycor() - -65) <= 20:
        # Exit
        clearMenu()
        exit()

b = startMenu()
b.goto(1000, 1000)


h = turtle.Turtle()
h.speed(0)
h.pu(); h.ht()

def hover(arg, x, y):
    h.clear()
    h.goto(x,y)
    h.color('grey')
    h.write(arg, move=False, align="left", font=("Open Sans", 30, "bold"))

clear = False

def clearMenu():
    global clear, b
    clear = True
    mouse.goto(1000, 1000)
    b.goto(1000, 1000)
    h.clear()
    b.clear()
    for a in view: a.ht()
    view.clear()


x, y = c.winfo_pointerx(), c.winfo_pointery()
def motion(event):
    x, y = event.x, event.y
    window()
    mousePosition = (x - (width)/2, -y + (height)/2 )
    mouse.goto(mousePosition)
    if abs(mouse.xcor() - -200) <= 40 and abs(mouse.ycor() - 75) <= 20:
        hover('PLAY', -250, 50) # Play
    elif abs(mouse.xcor() - -175) <= 90 and abs(mouse.ycor() - 5) <= 20:
        hover('OPTIONS', -250, -20) # Options
    elif abs(mouse.xcor() - -200) <= 40 and abs(mouse.ycor() - -65) <= 20:
        hover('EXIT', -250, -90) # Exit
    else:
        h.clear()
    mouse.goto(10000, 10000)
    
    
    
mouse = turtle.Turtle()
mouse.speed(0)
mouse.pu()
mouse.ht()

s.onscreenclick(click)


while not clear:
    window()
    for a in view:

        a.right(0.1)
        a.forward(0.5)

        if a.xcor() > width/2 or a.xcor() < - width/2:
            a.goto(-a.xcor(), random.randint(-height/2, height/2))
        elif a.ycor() < -height/2 or a.ycor() > height/2:
            a.goto(random.randint(-width/2, width/2), -a.ycor())
        
        if abs(a.xcor()) <= menuWidth/2 + 5 and abs(a.ycor()) <= menuHeight/2 + 5: a.ht()
        else: a.st()

    s.update()
    if not clear: c.bind('<Motion>', motion)


s.mainloop()