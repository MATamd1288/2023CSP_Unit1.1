#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
legs = 6
lengthoflegs = 70
degrees = 380 / legs
spider.pensize(5)
n = 0
while (n < legs):
  spider.goto(0, 0)
  spider.setheading(degrees * n)
  spider.forward(lengthoflegs)
  n = n + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()