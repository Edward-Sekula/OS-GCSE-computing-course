import random
let = ['a','b','c','d','e','f','g','h','i','j']
letstr = 'abcdefghij'
botship = []
shiplength = 5

playerguess=[]
botguess=[]

coordmem1=0
coordmem2=0
coordmem3=0
coordmem4=0

def ship():
    count2 = 1
    bob = []
    go = True
    while go == True:
        SL1 = shiplength//2
        SL2 = (SL1 + shiplength%2)
        count = 0
        if player == 'bot':
            numdex = random.randint(1,10)
            letdexnum = random.randint(0,9)
            updown = random.randint(1,2)
            check = bsl
        if player == 'player':
            if count2 > 1:
                print('please adjust midpoint coordinate')
            coord = input('input mindpoint coordinate\n')
            numdex = int(coord[1:len(coord)])
            letdexnum = letstr.find(coord[0])
            updown = int(input('1.up\n2.down\n'))
            count2 = count2 + 1
            check = psl
        if updown == 1:
            x = (numdex-SL1)
            y = (numdex+SL2)
            numlist = list(range(x,y))
            if all(i > 0 and i <= 10 for i in numlist):
                for k in range(len(numlist)):
                    numlist[count] = (str(numlist[count]))
                    numlist[count] = let[letdexnum] + numlist[count]
                    count = count+1
                if all(i not in check for i in numlist):                         
                    go = False
                    return numlist
                else:
                    if player == 'player':
                        print('error -- coordinate already occupied by a ship')
                    else:
                        print()
                        
        if updown == 2:
            x = letdexnum-SL1
            y = letdexnum+SL2
            letlist = list(range(x,y))
            if all(i >= 0 and i <10 for i in letlist):
                for k in  range (len(letlist)):
                    letlist[count] = let[letlist[count]]
                    letlist[count] = letlist[count] + str(numdex)
                    count = count+1
                if all(i not in check for i in letlist):                         
                    go = False
                    return letlist
                else:
                    if player == 'player':
                        print('error -- coordinate already occupied by a ship')
                    else:
                        print()
#-------------------------------------bot generation----------------------------------##
player = 'bot'

bsl = []
## carrier
##shiplength = 5 (line 5)
BCA = ship()
bcl.extend(BCA)
##battleship
shiplength = 4
BBS = ship()
bcl.extend(BBS)
##submarine
shiplength = 3
BSU = ship()
bcl.extend(BSU)
##destroyer
shiplength = 2
BDS = ship()
bcl.extend(BDS)
##-----------------------------------player generation--------------------------------##
player = 'player'

psl = []

shiplength = 5
PCA = ship()
psl.extend(PCA)
##battleship
shiplength = 4
PBS = ship()
psl.extend(PBS)
##submarine
shiplength = 3
PSU = ship()
psl.extend(PSU)
##destroyer
shiplength = 2
PDS = ship()
psl.extend(PDS)
##-----------------------------------acctual game-------------------------------------##
def PT():
    tf = True
    while tf==True:
        pg = input('input guess')
        if pg in playerguess:
            print('guessed already')
        else:
            tf = False
            playerguess.append(pg)
            return pg
def BT():
    tf = True
    while tf == True:
        numdex = random.randint(1,10)
        letdexnum = random.randint(0,9)
        bg = let[letdexnum] + str(numdex)
        if bg in botguess:
            pass
        else:
            tf = False
            botguess.append(bg)
            return bg
while len(psl)>0 and len(bsl)>0:
    BT()
    if len(psl)==0:
        print('bot won')
    else:
        PT()
        if len(bsl)==0:
            print('you won')
        else:
            pass
