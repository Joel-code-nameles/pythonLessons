import turtle

screen = turtle.Screen()
player = turtle.Turtle()

player.shape("turtle")
player.color("white", "black")
player.penup()
player.goto(-100, 100)

player2 = turtle.Turtle()
screen.addshape(r"C:\Users\Joel\Desktop\game\Day2\icegif-1479.gif")
player2.shape(r"C:\Users\Joel\Desktop\game\Day2\icegif-1479.gif")
player2.penup()
player2.goto(100, -100)

def move_up():
    player.setheading(90)
    player.forward(10)

def move_down():
    player.setheading(270)
    player.forward(10)

def move_left():
    player.setheading(180)
    player.forward(10)

def move_right():
    player.setheading(0)
    player.forward(10)



def move_up2():
    player2.setheading(90)
    player2.forward(10)

def move_down2():
    player2.setheading(270)
    player2.forward(10)

def move_left2():
    player2.setheading(180)
    player2.forward(10)

def move_right2():
    player2.setheading(0)
    player2.forward(10)



screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_right, "Right")
screen.onkey(move_left, "Left")

screen.onkey(move_up2, "w")
screen.onkey(move_down2, "s")
screen.onkey(move_right2, "d")
screen.onkey(move_left2, "a")

screen.mainloop()