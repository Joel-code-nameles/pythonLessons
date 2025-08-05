import  turtle
import random

game_win = turtle.Screen()
game_win.title("Catch The food")
game_win.bgcolor("lightgreen")

character = turtle.Turtle()
character.shape("turtle")
character.color("black")
character.penup()

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.speed(8)

def move_food():
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    food.goto(x,y)
move_food()

def move_up():
    character.setheading(90)
    character.forward(20)
    check_food()

def move_down():
    character.setheading(270)
    character.forward(20)
    check_food()

def move_right():
    character.setheading(0)
    character.forward(20)
    check_food()

def move_left():
    character.setheading(180)
    character.forward(20)
    check_food()

def check_food():
    if character.distance(food) <20:
        move_food()


game_win.listen()
game_win.onkey(move_up, "Up")
game_win.onkey(move_down, "Down")
game_win.onkey(move_right, "Right")
game_win.onkey(move_left, "Left")
game_win.mainloop()




