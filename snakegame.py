"""
Joc de Snake, projecte de Pol Raich de l'asignatura Algorismia i programació audiovisual en l'universitat politecnica de catalunya

"""

import turtle
import random
import time

posponer = 0.05


# Screen Configuration
window = turtle.Screen()
window.bgpic("img\Background.gif")
window.title("Snake Game")
window.setup(width = 1000, height = 700)
window.tracer(0)



# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape('square')                # Def size 20 x 20 px
head.color("#19A844")
head.penup()                        # Removes the trail of the turtle
head.goto(0,0)                      # Centers the head of the snake
head.direction = 'stop'

# Food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('#F25BEB')
food.penup()
food.goto(random.randint(-480, 480), random.randint(-320,280))                    # The food has to spawn between -500, 500 and letting a margin of 20px for not beeing in the border.

# Snake Body
body = []
body_color = [("#63E066"),("#8BE051"),("#6AE0A6"),("#91E080")]

#Text Printed
text = turtle.Turtle()
text.speed(0)
text.color("#3E0C65")
text.penup()
text.hideturtle()
text.goto(0, 310)
text.write('Puntos: 0                      Puntos Maximos: 0', align='center', font=("Arial", 20, "normal"))

points = 0
maxpoints = 0


def printtext():
    """
    
    """
    global points
    global maxpoints
    
    if points > maxpoints:
        maxpoints = points
        
    text.clear()
    text.write(f'Puntos: {points}                       Puntos Maximos: {maxpoints}', align='center', font=("Arial", 20, "normal"))


# Movements
def move_up():
    head.direction = 'up'
  
    
def move_down():
    head.direction = 'down'

    
def move_left():
    head.direction = 'left'
 
    
def move_right():
    head.direction = 'right'


def movment():
    """
    
    """
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)
        
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)
        
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)


def IncraseSnakeSize():
    """
    
    """
    global points
    part = turtle.Turtle()
    part.speed(0)
    part.shape('square')
    part.color(random.choice(body_color))
    part.penup()
    body.append(part)
    points += 1
    printtext()


def Bodymovment():
    """
    
    """
    Body_len = len(body)
    
    for part in range(Body_len - 1, 0, -1):
        x = body[part - 1].xcor()
        y = body[part - 1].ycor()
        body[part].goto(x, y)
    
    if Body_len > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x, y)
        
    

def Eatfood():
    """
    
    """
    if head.distance(food) < 20:
        food.goto(random.randint(-480, 480), random.randint(-320, 280))
        IncraseSnakeSize()  
        
        
def Border():
    """
    
    """
    global points
    
    if head.xcor() > 480 or head.ycor() > 280 or  head.xcor() < -480 or head.ycor() < -320 :
        time.sleep(0.5)
        head.direction = 'stop'
        head.goto(0, 0)
        for part in body:             
            part.goto(1000,1000)
            
        body.clear()
        points = 0
        printtext()
        
def eat():
    """
    
    """
    global points
    for part in body:
        if head.distance(part) < 20:
            time.sleep(0.5)
            head.goto(0, 0)
            head.direction = 'stop'
            for part in body:
                part.goto(1000, 1000)
            
            body.clear()
            printtext()
        
        
# Keyboard conexion
window.listen()
window.onkeypress(move_up,'Up')
window.onkeypress(move_left,'Left')
window.onkeypress(move_down,'Down')
window.onkeypress(move_right,'Right')
window.onkeypress(move_up,'w')
window.onkeypress(move_left,'a')
window.onkeypress(move_down,'s')
window.onkeypress(move_right,'d')

while True:
    window.update()
    
    Border()
    Eatfood()
    eat()
    Bodymovment()
    movment()
    
    time.sleep(posponer)
