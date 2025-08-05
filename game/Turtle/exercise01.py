import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
t.color("blue", "orange")
t.begin_fill()
t.pensize(2)
t.speed(3)

for _ in range(1):
    t.circle(100)
    t.penup()
    t.goto(-100, 100)
    t.pendown()
    t.circle(60)
    t.penup()
    t.goto(100, -70)
    t.pendown()
    t.circle(60)

t.end_fill()
screen.mainloop()