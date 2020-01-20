num = ['123456789']
def inc_cm():
    count = (0)
    z = ()
    inc = input('enter input')
    for k in range(len(inc)):
        if inc[count] in num:
            z1 = (inc[count])
            z2 = (z2+z1)
            print()
            z = float(z2)
    y = (z*2.54)
    print(y,'cm')
def cm_inc():
    inc = int(input('enter input'))
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

