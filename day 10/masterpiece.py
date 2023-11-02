import turtle
import random

# Set up the turtle


screen = turtle.Screen()
turtle.speed(20)

# Function to draw a random pattern
def draw_random_pattern():
    for _ in range(100):  # You can adjust the number of steps
        turtle.forward(random.randint(108, 108))  # Adjust the range of distances
        turtle.left(random.randint(108, 108))  # Adjust the range of angles
        
        
        
  # Adjust the range of angles
# Draw the random pattern
draw_random_pattern()

# Close the window when clicked

screen.exitonclick()


