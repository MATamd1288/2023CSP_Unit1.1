import turtle as trtl

painter = trtl.Turtle()

painter.speed(100)

painter.penup()

x = -100
y = 0
painter.goto(x,y)

painter.pendown()

for triangle in range(15):
    painter.forward(50)
    painter.left(120)
    painter.left(45)

    x += 50
    y += 50
    painter.goto(x, y)


wn = trtl.Screen()
wn.mainloop()