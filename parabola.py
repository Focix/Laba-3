import turtle as tr
import numpy as np
tr.screensize(1000, 1000)
tr.shape('circle')
x = -500
y = 0
v = 50
tr.penup()
tr.goto(x, y)
tr.pendown()
alpha = np.pi / 3
vx = v * np.cos(alpha)
vy = v * np.sin(alpha)
ay = - 10
dt = 0.1
for i in range(500):
    x += vx * dt
    y += vy * dt + ay * (dt ** 2) / 2
    if  y <= 0.8:
        vy = - vy * 0.9
        if  np.abs(vy) < 0.5:
            break
    vy += ay * dt
    tr.goto(x, y)
tr.done()