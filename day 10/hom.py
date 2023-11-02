import turtle
import random

turtle.width(0.5)

screen = turtle.Screen()
screen.bgcolor("white")
turtle.speed(2000000000)


def  draw_random_patern() :

 for _ in range (1000) :
    turtle.forward(random.randint(103,104,))
    turtle.right(random.randint(105,106,))
    
    


draw_random_patern() 
        
   
   
screen.exitonclick()