def inc_cm():
    z = input('enter input')
    c = z.find(' ')
    print(c)
    while True:
        if c == (-1):
            print ('error')
            z = input('enter input')
            c = z.find(' ')
        else:
            k = (c)
            f = z[0:k]
            print(f)
            u = int(f)
            y = (u*2.54)
            print(y,'cm')
            break
def cm_inc():
    z = input('enter input')
    c = z.find(' ')
    while True:
        if c == (-1):
            print ('error')
        else:
            k = (c)
            f = z[0:k]
            print(f)
            u = int(f)
            y = (z/2.54)
            print(y,'"')
            break

    
teat = ('1.inches to cm\n2.cm to inches\n3.quit\n')
print(teat)
num = ('1234567890')
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
