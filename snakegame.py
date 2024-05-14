"""
Joc de Snake, projecte de Pol Raich i Victor Pàllas de l'asignatura Algorismia i programació audiovisual en l'universitat politecnica de catalunya

"""

import turtle
import random
import time

difficulty = 0.05 
posponer = difficulty               # Speed of the snake


# Screen Configuration
window = turtle.Screen()
window.bgcolor("lightgreen")
window.title("Snake Game")
window.setup(width = 1000, height = 600)


# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape('square')                # Def size 20 x 20 px
head.color("blue")
head.penup()                        # Removes the trail of the turtle
head.goto(0,0)                      # Centers the head of the snake
head.direction = 'stop'

# Food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(random.randint(-480, 480), random.randint(-280,280))                    # The food has to spawn between -500, 500 and letting a margin of 20px for not beeing in the border.

# Body
body = []


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
    part = turtle.Turtle()
    part.speed(0)
    part.shape('square')
    part.color('yellow')
    part.penup()
    body.append(part)


def Bodymovment():
    """
    
    """
    
        
    

def Eatfood():
    """
    
    """
    if head.distance(food) < 20:
        IncraseSnakeSize()  
        food.goto(random.randint(-480, 480), random.randint(-280, 280))
        
        
def Border():
    if head.xcor() > 480 or head.ycor() > 280 or  head.xcor() < -480 or head.ycor() < -280 :
        head.direction = 'stop'
        head.goto(0, 0)
        body.clear()
        
        
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
    
    movment()
    Eatfood()
    Border()
    Bodymovment()
    
    time.sleep(posponer)
