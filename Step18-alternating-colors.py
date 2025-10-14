#   a113_tower.py
#   Modify this code in VS Code to alternate the colors of the 
#   floors every three floors
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -150
y = -150

# height of tower and a counter for each floor
num_floors = 51

# iterate
for floor in range(num_floors):
  # set placement and color of turtle
  painter.penup()
  painter.goto(x, y)
 # painter.color("gray")

   
  if floor % 6 > 2:
    painter.color("blue")
  else:
    painter.color("gray")
   
  #draw the floor
  painter.pendown()
  painter.forward(50)
  y = y + 5 # location of next floor
  

# painter.pensize(5)
# x = -50
# y = -150

# num_floors = 51

# for floor in range(num_floors):
#   painter.penup()
#   painter.goto(x, y)
  
#   if floor % 6 > 2:
#     painter.color("blue")
#   else:
#     painter.color("gray")
    
#   painter.pendown()
#   painter.forward(50)
#   y = y + 5

wn = trtl.Screen()
wn.mainloop()
