import turtle

screen = turtle.Screen()
draw = turtle.Turtle()

draw.penup()
draw.goto(-100, 100)
draw.pendown()
draw.write("Joel A. Asare", font=("Conservation",15,"bold"))

screen.mainloop()