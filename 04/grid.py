import turtle

count1 = 0
count2 = 0

while (count1 < 6):
    y_loc = count1 * 100
    turtle.penup()
    turtle.goto(0,y_loc)
    turtle.pendown()
    turtle.forward(500)
    count1 += 1

turtle.left(90)

while (count2 < 6):
    x_loc = count2 * 100
    turtle.penup()
    turtle.goto(x_loc, 0)
    turtle.pendown()
    turtle.forward(500)
    count2 += 1

turtle.exitonclick()
