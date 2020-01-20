ps = (501)
p2s = (501)

while True:
    player = int(input())
    x = int(input('enter your scores\n'))
    y = int(input())
    z = int(input())
    if player ==(1):
        c = (x+y+z)
        if (ps-c)>=1:
            ps = (ps-c)
            print(ps)
        else:
            if ps-c == 0:
                print('p1 wins')
    elif player ==(2):
        c = (x+y+z)
        if (ps-c)>=1:
            ps = (ps-c)
            print(ps)
        else:
            if ps-c == 0 or ps - x == 0:
                
                print('p1 wins')
            elif ps - y == 0 or ps - z ==0:
                print ('p2 wins')
