import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

x = -150
y = -150

num_tower = 3
num_floors = 63

for floor in range(num_floors):
  
  if floor % 21 == 0:
    x = x + 80
    y = -150

  painter.penup()
  painter.goto(x, y)

  if floor % 6 > 2:
    painter.color("blue")
  else:
    painter.color("gray")
   
  painter.pendown()
  painter.forward(50)
  y = y + 5
  
wn = trtl.Screen()
wn.mainloop()
