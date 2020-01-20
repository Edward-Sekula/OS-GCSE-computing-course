import random
d1 = (random.randint(1,6))
d2 = (random.randint(1,6))
d3 = (random.randint(1,6))

print(d1,d2,d3)
if d1==d2 and d1==d3:
    print(d1+d2+d3)
else:
    if d1!=d2 and d2!=d3:
        print('score is 0')
    else:
        if d1==d2:
            print(d1+d2)
        if d1==d3:
            print(d1+d3)
        else:
            print(d2+d3)



    
