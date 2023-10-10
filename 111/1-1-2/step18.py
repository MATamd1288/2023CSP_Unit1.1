# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()

# set the pen and fill colors
# then draw a circle
painter.pencolor("blue")
painter.fillcolor("red")
painter.begin_fill()
painter.circle(100)
painter.end_fill()


# move the turtle to another part of the screen
painter.penup()
painter.goto(150,150)
painter.pendown()

# change both the pen and fill colors
painter.pencolor("pink")
painter.fillcolor("green")
# then draw a polygon of your choice
painter.circle(100,360,8)

# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()