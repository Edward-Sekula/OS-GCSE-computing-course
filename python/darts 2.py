player = 1
m = ()
def player1():
    ps = (501)
    c = (x+y+z)
    if (ps-c)>=1:
        ps = (ps-c)
        print(ps)
        player = 2
        print (player)
    else:
        if ps-c == 0 or ps - x == 0:
            print('p1 wins')
            m = ('do you want to play again?')
        elif ps - y == 0 or ps - z ==0:
            print ('p1 wins')
            m = ('do you want to play again?')

def player2():
    ps2 = (501)
    c = (x+y+z)
    if (ps2-c)>=1:
        ps2 = (ps2-c)
        print(ps2)
        player = 1
    else:
        if ps2-c == 0 or ps2 - x == 0:
            print('p2 wins')
            m = ('do you want to play again?')
        elif ps2 - y == 0 or ps2 - z ==0:
            print ('p2 wins')
            m = ('do you want to play again?')

while True:
    x = int(input('enter your scores\n'))
    y = int(input())
    z = int(input())
    if player==1:
        player1()
    elif player==2:
        player2()
    

