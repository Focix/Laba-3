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

with open('input', 'w') as writing:
    for i in one:
        print(*i,end='/', sep=',', file=writing)
    print(file=writing)
    for i in four:
        print(*i,end='/', sep=',', file=writing)
    print(file=writing)
    for i in seven:
        print(*i, end='/', sep=',', file=writing)
    print(file=writing)
    for i in zero:
        print(*i, end='/', sep=',', file=writing)

with open('input', 'r') as writing:
    A=[]
    for line in writing:
        line = line.rstrip()
        A = line.split('/')
        A.pop()
        for i in range(len(A)):
            A[i] = A[i].split(',')
            A[i][0] = int(A[i][0])
            A[i][1] = int(A[i][1])
        print(A)
        number(A)
    tr.done()