from random import *
import turtle as tr
tr.shape('turtle')
for i in range(200):
    tr.forward(50 * random())
    tr.left(randint(0,360))
tr.done()
