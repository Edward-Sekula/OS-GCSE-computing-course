import random
miss = 0
hits = 0
battleshipps = []
let = ['a','b','c','d','e','f','g','h','i','j']
ch = []
ps = input('input ship position')
missed = []
def guess():
    pdd = random.choice(let)
    pd = random.randint(1,10)
    ks = (pdd+str(pd))
class botship():
    def carrier():
        go = True
        while go == True:
            pdd = random.choice(let)
            pd = random.randint(1,10)
            ks = (pdd+str(pd))
            updown = rand.randint(1,2)
            carrierindex = []
            if updown == 1:#up2)
                carrierindex.append(pd+2)
                carrierindex.append(pd+1)
                carrierindex.append(pd)
                carrierindex.append(pd-1)
                carrierindex.append(pd-2)
                if all(i > 0 for i in carrierindex):
                    print('yay')
                else:
                    print()
carrier()
##    if ks in battleshipps:
##        choos()
##    else:
##        battleshipps.append(ks)
##go = True
##while go == True:
##    ks = choos()
##    print(ks)
##    if ks in ch:
## # resets to while
##        print() 
##    elif go == True:
##        ch.append(ks)
##        x = input('input coorinate')
##        if x in missed:
##            print('already chosen -- try again')
##        elif x == bs:
##            print('yay')
##            go = False
##            hits = hits +1
##        else:
##            print('miss')
##            miss = miss+1
##            missed.append(x)
###---------------bot turn----------------------------------#
##        if ks == ps :
##            print('bot wins')
##            go = False
##        elif:
##            print()
##        
##    print(miss,' misses ',hits,' hits')
##


