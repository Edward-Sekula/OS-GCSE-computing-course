import random
score = (0)
print(score)
for k in range(1,11):
    x = random.randint(1,10)
    y = random.randint(1,10)
    a = ['+','/','*','-']
    n = random.choice(a)
    z = x, n, y
    h = int(input(z))
    if n == '+':
        p = (x+y)
        if h == p:
            score = (score+1)
        else:
            print('wrong')
    if n == '/':
        p = (x/y)
        if h == p:
            score = (score+1)
        else:
            print('wrong')
    if n == '*':
        p = (x*y)
        if h == p:
            score = (score+1)
        else:
            print('wrong')
    if n == '-':
        p = (x-y)
        if h == p:
            score = (score+1)
        else:
            print('wrong')
