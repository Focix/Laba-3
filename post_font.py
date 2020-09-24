import turtle as tr

def number(X):
    global delta
    tr.penup()
    tr.goto(X[0][0] + delta, X[0][1])
    tr.pendown()
    for i in X:
        tr.goto(i[0] + delta, i[1])
    tr.penup()
    tr.goto(X[len(X)- 1][0] + delta + 20,X[len(X)- 1][1])
    tr.pendown()
    delta += 40
    return None

delta = 0
tr.shape('turtle')
one = [(0,0), (20, 20), (20, -20), (20, 20)]
four = [(0, 20), (0, 0), (20, 0), (20, -20), (20, 20)]
seven = [(0, 20), (20, 20), (0, 0), (0, -20), (0, 0), (20, 20)]
zero = [(0, 20), (0, -20), (20, -20), (20, 20), (0, 20), (20, 20)]
number(one)
number(four)
number(one)
number(seven)
number(zero)
number(zero)
tr.done()