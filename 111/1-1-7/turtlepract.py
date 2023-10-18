import turtle as trtl

jack = trtl.Turtle()
Randy = trtl.Turtle()
James = trtl.Turtle()
josh = trtl.Turtle()
zach = trtl.Turtle()

turtlelist = {jack,Randy,James,josh,zach}

x = -100
y = 0

for turtle in turtlelist:
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    x = x + 30

print (turtlelist)

wn = trtl.Screen()
wn.mainloop()