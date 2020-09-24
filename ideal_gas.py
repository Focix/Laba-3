from random import randint
import turtle
import numpy as np

turtle.penup()
turtle.goto(300, -300)
turtle.pendown()
turtle.left(90)
for i in range(4):
    turtle.forward(600)
    turtle.left(90)
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.hideturtle()

number_of_turtles = 10
steps_of_time_number = 100
dt = 0.1


pool = [[turtle.Turtle(shape='circle'),  randint(0, 360), randint(20, 70)] for i in range(number_of_turtles)]
        # объект, угол и скорость
for unit in pool:
    unit[0].penup()
    unit[0].speed(50)
    unit[0].goto(randint(-250, 250), randint(-250, 250))

for i in range(steps_of_time_number):
    for unit in pool:
        unit_xpos = unit[0].xcor()
        unit_ypos = unit[0].ycor()
        for hit_unit in pool: # проверка на соударение
            hit_xpos = hit_unit[0].xcor()
            hit_ypos = hit_unit[0].ycor()
            if hit_unit != unit and (((hit_xpos - unit_xpos) ** 2 + (hit_ypos - unit_ypos) ** 2) < 250):
                unit[1], hit_unit[1] = hit_unit[1], unit[1]
                unit[2], hit_unit[2] = hit_unit[2], unit[2]
                unit[0].goto(unit_xpos + unit[2] * np.cos(unit[1]) * dt,
                             unit_ypos + unit[2] * np.sin(unit[1]) * dt)
                hit_unit[0].goto(hit_xpos + hit_unit[2] * np.cos(hit_unit[1]) * dt,
                                 hit_ypos + hit_unit[2] * np.sin(hit_unit[1]) * dt)
        if np.abs(unit_xpos + unit[2] * np.cos(unit[1]) * dt) >= 300: # проверка на удар в вертикальные стенки
            unit[1] = 180 - unit[1]
        if np.abs(unit_ypos + unit[2] * np.sin(unit[1]) * dt) >= 300: # проверка на удар в горизонтальные стенки
            unit[1] = - unit[1]
        unit[0].goto(unit_xpos + unit[2] * np.cos(unit[1]) * dt, unit_ypos + unit[2] * np.sin(unit[1]) * dt)
