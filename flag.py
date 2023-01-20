import turtle
import pyautogui
# Set size of the turtle window to be the size of the screen
xScreen, yScreen = pyautogui.size()
turtle.screensize(xScreen, yScreen)
turtle.setup(xScreen, yScreen)

# Set size
size = xScreen / 250

# Flag dimensions
length = 190 * size
width = 100 * size
stripe = width / 13
starDiameter = width * 0.0616
starSide = starDiameter * (17.8/19)
F = width * 0.054
H = width * 0.063

# Turn off screen updates (optional)
#turtle.tracer(0, 0)

# Set the turtle's speed to the maximum value
turtle.speed(0)

# Set the starting position for the turtle
turtle.penup()
turtle.goto(length / 2, width / 2)
turtle.pendown()

# Set the background color to grey
turtle.bgcolor("grey")

# Create a variable to keep track of the current color
current_color = "#BB133E"

# Use a for loop to draw the rectangles
for i in range(13):
  # Set the turtle's color to the current color
  turtle.color(current_color)

  # Draw the rectangle
  turtle.begin_fill()
  turtle.left(90)
  turtle.forward(stripe)
  turtle.left(90)
  turtle.forward(length)
  turtle.left(90)
  turtle.forward(stripe)
  turtle.left(90)
  turtle.forward(length)
  turtle.end_fill()

  # Move the turtle to the next position
  turtle.penup()
  turtle.right(90)
  turtle.forward(stripe)
  turtle.left(90)
  turtle.pendown()

  # Update the current color
  if current_color == "#BB133E":
    current_color = "white"
  else:
    current_color = "#BB133E"

# Move to draw corner blue rectangle
turtle.penup()
turtle.left(180)
turtle.forward(length)
turtle.right(90)
turtle.forward((stripe * 7) + 1)
turtle.right(90)

# Set the turtle's color old navy blue
turtle.color("#002147")

# Draw the rectangle
turtle.pendown()
turtle.begin_fill()
turtle.forward(length * 0.4)
turtle.left(90)
turtle.forward((stripe * 7) - 1)
turtle.left(90)
turtle.forward(length * 0.4)
turtle.left(90)
turtle.forward((stripe * 7) - 1)
turtle.end_fill()

# Draw the stars
turtle.penup()
turtle.color("white")

# Move to first star of 6 x 5 rows
turtle.left(180)
turtle.forward((stripe * 7) - 1 - (width * 0.05385))
turtle.right(90)
turtle.forward(H - (starSide * 0.5))

for i in range(5):
    for _ in range(6):
        turtle.pendown()
        turtle.begin_fill()
        for _ in range(5):
            turtle.forward(starSide)
            turtle.right(144)
        turtle.end_fill()
        turtle.penup()
        turtle.forward(H * 2)
    turtle.left(180)
    turtle.forward(H * 12)
    turtle.left(90)
    turtle.forward(F * 2)
    turtle.left(90)

# Move to first star of 5 x 4 rows
turtle.left(90)
turtle.forward(F * 9)
turtle.right(90)
turtle.forward(H)

for i in range(4):
    for _ in range(5):
        turtle.pendown()
        turtle.begin_fill()
        for _ in range(5):
            turtle.forward(starSide)
            turtle.right(144)
        turtle.end_fill()
        turtle.penup()
        turtle.forward(H * 2)
    turtle.left(180)
    turtle.forward(H * 10)
    turtle.left(90)
    turtle.forward(F * 2)
    turtle.left(90)

turtle.hideturtle()

# Update the screen (optional)
#turtle.update()

# Keep the turtle window open until it is closed
turtle.mainloop()