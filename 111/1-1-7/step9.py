#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)

# sets up the variables for the turtle to go to the starting position
startx = 0
starty = 0

#turtle goes to the starting position
for t in my_turtles:
  t.goto(startx, starty)
  t.right(45)
  t.forward(50)
  t.penup()
  start_x = t.xcor()
  start_y = t.ycor()

#turtle starting position changes
  startx = startx + 50
  starty = starty + 50

wn = trtl.Screen()
wn.mainloop()