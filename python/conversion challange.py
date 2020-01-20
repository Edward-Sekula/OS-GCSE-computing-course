def inc_cm():
    z = int(input('enter input'))
    y = (z*2.54)
    print(y,'cm')
def cm_inc():
    z = int(input('enter input'))
    y = (z/2.54)
    print(y,'"')
    
y = ('1.inches to cm\n2.cm to inches\n3.quit\n')
print(y)
while True:
    x = int(input())
    if x>=1 and x<=3:
        if x == 1:
            inc_cm()
        elif x == 2:
            cm_inc()
        elif x ==3:
            break
    else:
        print('Invalid input, try again')
        print (y)

