# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()

# add code here for a circle
painter.circle

# move the turtle to another part of the screen
painter.penup()
painter.goto(x 44, y 50)
painter.pendown()
# add code here for an arc
painter.circle(radius: 20, extent: 50)

# move the turtle to another part of the screen
painter.penup()
painter.goto(x 44, y 50)
painter.pendown()

# add code here for an arc that is greater than 90 degrees and has 5 steps
painter.circle(radius: 20, extent: 50, steps: 5)

# move the turtle to another part of the screen
painter.penup()
painter.goto(x 44, y 50)
painter.pendown()

# add code here to create a polygon of your choice using the circle method
painter.circle(radius: 20, extent: 50, steps: 5)

# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()

