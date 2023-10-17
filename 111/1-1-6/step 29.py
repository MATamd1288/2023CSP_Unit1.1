#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
spider.pensize(40)
# spider body
spider.circle(20)
# amt of legs and spacing
legs = 8
lengthoflegs = 70
degrees = 360 / legs - 20
spider.pensize(5)
n = 0
# draw legs
while (n < legs):
  spider.goto(0, 20)
  if (n < 4):
    spider.setheading(degrees * n - 45)
  else:
    spider.setheading(degrees * n + 45)
  spider.forward(lengthoflegs)
  n = n + 1

spider.penup()
spider.goto(6,27 )
spider.pendown()
spider.color ("white")
spider.pensize(10)
spider.circle(5)
spider.penup()
spider.goto(-20,27 )
spider.pendown()
spider.circle(5)

spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()