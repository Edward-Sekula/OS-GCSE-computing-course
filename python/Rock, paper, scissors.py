import random
print('rock,paper,scissors')
ch = ('r','p','s')
ps = (0)
cs = (0)

while True:
    if ps<10 and cs<10:
        x = input()
        y = x[0].lower()
        z = random.choice(ch)
        if y == ('r') and z == ('s') or y == ('p') and z == ('r') or y == ('s') and z == ('p'):
            print('you won!')
            ps = (ps+1)
            print('rock,paper,scissors')
        if z == ('r') and y == ('s') or z == ('p') and y == ('r') or z == ('s') and y == ('p'):
            print('I won')
            cs = (cs+1)
            print('rock,paper,scissors')
        else:
            print('tie')
            print('rock,paper,scissors')
    elif ps==10:
        print('you won',ps,'to',cs )
        break
    elif cs==10:
        print('I won',cs,'to',ps)
        break
