from turtle import Turtle,Screen

timmy=Turtle()  #klasse auf rufen
#timmy.shape("turtle") # shape() : um den zieger zu aendern
#timmy.color("orange")    # um color zu aendern
#timmy.width(20) px
# squer
"""for _ in range(4):
    timmy.forward(100)     # zahen schriette nach recht
    timmy.left(90)"""



#Draw a Dashed Line
"""for item in range(100):
    timmy.forward(5)
    timmy.penup()
    timmy.forward(5)
    timmy.pendown()"""
"""
colors = ["red", "dark red", "firebrick", "orange", "dark orange", "gold", "yellow", "dark khaki", "green", "lime green", "dark green", "turquoise", "light sea green", "deep sky blue", "blue", "medium blue", "dark blue", "purple", "medium purple", "dark magenta"]
import random
def draw_sape(num):
    angle=360/num
    for _ in range(num):
        timmy.forward(100)
        timmy.left(angle)
for shape in range(3,11):
    timmy.color(random.choice(colors))
    draw_sape(shape)
"""
"""
timmy.speed("fastest")
import random
def randoma_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color = (r,g,b)
    return color
x_min,x_max = -200,200
y_min,y_max = -200,200
timmy.width(5)
screen=Screen()
screen.colormode(255)
move=[0,90,280,270]
for _ in range(100):
    timmy.color(randoma_color())
    timmy.forward(30)
    timmy.setheading(random.choice(move))
    x,y=timmy.pos()
    if x<x_min or x>x_max or y<y_min or y>y_max:
        timmy.goto(-200,0)
"""

timmy.speed("fastest")
import random
def randoma_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color = (r,g,b)
    return color
x_min,x_max = -200,200
y_min,y_max = -200,200
timmy.width(2)
screen=Screen()
screen.colormode(255)
num=0
for i in range(100):
    timmy.color(randoma_color())
    timmy.circle(90)
    num +=5
    timmy.setheading(num)
    x,y=timmy.pos()
    if x<x_min or x>x_max or y<y_min or y>y_max:
        timmy.goto(-200,0)









screen.exitonclick() # um das fenster bei click zu schliessen
