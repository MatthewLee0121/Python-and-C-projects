import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a Turtle object
stickman = turtle.Turtle()
stickman.speed(2)

# Drawing the stickman
def draw_circle(color, radius, x, y):
    stickman.penup()
    stickman.fillcolor(color)
    stickman.goto(x, y)
    stickman.pendown()
    stickman.circle(radius)

draw_circle("black", 50, 0, -50)  # Head
stickman.right(90)
stickman.forward(100)  # Body
stickman.right(30)
stickman.forward(40)  # Right arm
stickman.backward(40)  # Reset
stickman.left(60)
stickman.forward(40)  # Left arm
stickman.backward(40)  # Reset
stickman.left(30)
stickman.backward(70)  # Body
stickman.left(30)
stickman.forward(50)  # Right leg
stickman.backward(50)  # Reset
stickman.right(60)
stickman.forward(50)  # Left leg

stickman.hideturtle()
turtle.done()