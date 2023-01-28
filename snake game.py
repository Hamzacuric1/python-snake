import turtle
import time

delay = 0.1
#pozadina
sg = turtle.Screen()
sg.title('Snake Game by Hamza Curic')
sg.bgcolor('green')
sg.setup(width=600, height=600)
sg.tracer(0)
sg.mainloop()

#glava
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('black')
head.penup()
head.goto(0,0)
head.direction = 'up'

#Fuctions
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.sety(y + 20)

    if head.direction == "right":
        x = head.xcor()
        head.sety(y + 20)

#Main game loop
while True:
    sg.update()

    move()

    time.sleep(delay)

sg.mainloop()
