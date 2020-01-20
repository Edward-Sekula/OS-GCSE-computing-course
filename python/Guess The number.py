import random
x = random.randint(1,100)
print('Guess the Number')
c = (1)
while True:
    y = int(input())
    x!=y
    if x == y:
        print('correct, you had ',c,' guesses')
    if y<x:
        print('higher')
    if y>x:
        print('lower')
    c = (c+1)
