import random

def turn(player,playerscore):
    print(player)
    go=True
    while go==True:
        playerscore = playerscore
        input('press ENTER to continue...')
        d1 = random.randint(1,5)
        d2 = random.randint(1,5)
        if d1 == 2 or d2 == 2 or d1 == 5 or d2 ==5:
            if d1 == 2 and d2 == 2:
                print('double trotter -- 20 points\n')
                playerscore = (playerscore+20)
            elif d1 == 4 or d2 == 4:
                if d1 == d2:
                    print('double snouter -- 20 points/n')
                    playerscore = (playerscore+20)
                else:
                    print('snouter -- 5 points\n')
                    playerscore = (playerscore+5)
            elif d1 == 5 or d2 == 5:
                if d1 == d2:
                    print('double Razor back -- 20 points\n')
                    playerscore = (playerscore+20)
                else:
                    print('razor back -- 5 points\n')
                    playerscore = (playerscore+5)       
            else:
                print('trotter -- 5 points\n')
                playerscore = (playerscore+5)
        elif d1 == d2:
            print('sider--1 point\n ')
            playerscore = (playerscore + 1)
        else:
            print('unlucky\n')
        go = False
    return playerscore

player1name="player1"
player2name="player2"
p1score=0
p2score=0
while p1score<40 and p2score<40:
    p1score=turn(player1name,p1score)
    if p1score<40:
        p2score=turn(player2name,p2score)
if p1score>20:
    print("p1 win")
else:
    print("p2 wins")
