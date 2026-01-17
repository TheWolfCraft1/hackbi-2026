#!/usr/bin/python
#^ignore this, it's called a shebang and is used to run the script as an executable in linux systems
#Note: apt package python3-tk is required to run program on linux systems
import turtle as trtl
from random import randint
wn = trtl.Screen()
from time import sleep
+362880

#percentage
tax = 3

print(randint(1,5))

print("Hello World")
#https://prod.liveshare.vsengsaas.visualstudio.com/join?EED0943644FEFCDB4EE1954B8AE1DBEBB138

'''
Restaurant game:
1. Customer walks to table
2. Server takes order
3. Time passes
4. Server brings food to table
5. Server comes for the bill
6. Server leaves
7. Customer leaves
'''

'''
Jvascript example:
var t = 5
var t = t+7

for (var i = 0; i < 10; i++) {
    console.log(i)
}   

'''
#Gabe's menu functions
'''


foods = {
    "burgir"; 5.99,
    "stak": 11.99,
    "sail lad": 6.99
    }
sides = {
    "fries": 2.99,
    "noogets": 3.99,
    }
def get_total(food, side1, side2):
    total = 0
    total += foods[food]/100*tax
    total += sides[side1]/100*tax
    total += foods[side2]/100*tax
    return total

'''






#text

occasion = (input("nam?: "))
name = (input("list a price: "))


# write out the celebration
celebration = trtl.Turtle()
celebration.hideturtle()
FONTSIZE = 40
FONT = ('Times New Roman', FONTSIZE, 'normal')
celebration.pencolor("#5bb1eb")
celebration.penup()
celebration.goto(-300,0)
celebration.pendown()
celebration.write(f'Happy {occasion}, {name}!', font=FONT)

###Outline:

#Walls + table:
walls = trtl.Turtle()


walls.pencolor("#9928E4")
 
walls.penup()
walls.goto(-400,-400)
walls.pendown()

walls.forward(450)
walls.right(90)

walls.forward(450)
walls.right(90)

walls.forward(450)
walls.right(90)

walls.forward(450)
walls.right(90)



            le()
            
table.penup()
table.goto(-350,-350)
table.pendown()

table.fillcolor("")
table.begin_fill()

table.circle(30)

table.end_fill()


#Create movable turtle with either wasd or arrow keys
#Remember to cancel imput if turtle is about to hit a wall

#Add a conditional that runs "pass" if the turtle moves into a colored spot near the table

#

while True:
    pass
wn.mainloop()

:
    sleep(1)