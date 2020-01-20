import random

def turn(player,playerscore):
    print(player)
    go=True
    while go==True:
        runscore1 = 0
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        runscore1 = (runscore1+d1+d2)
        print(d1,' and ',d2)
        if d1 == 1 or d2 == 1:
            runscore1 = 0
            print('snakeeyes no score')
            if d1 ==1 and d2==1:
                print('banked score set to zero')
                p1ayerscore=0
                go=False
            else:
                print('you lost running total set to zero')
                go=False
        else:
            x = int(input('1.bank\n2.gamble\n'))
            if x == 1:
                playerscore = playerscore+runscore1
                runscore1 = 0
                go=False
                
            elif x == 2:
                print('gamble')
    return playerscore

player1name="player1"
player2name="player2"
p1score=0
p2score=0
while p1score<20 and p2score<20:
    p1score=turn(player1name,p1score)
    if p1score<20:
        p2score=turn(player2name,p2score)
if p1score>20:
    print("p1 win")
else:
    print("p2 wins")
