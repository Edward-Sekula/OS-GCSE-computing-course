x = int(input('input num 1'))
y = int(input('input num2'))

if x<y:
    print('the largest number is ',y)
if x>y:
    print('the largest number is ',x)
if x==y:
    print('the numbers are equel')

nitrate = float(input('input the nitrate level'))
if nitrate<=50:
    if nitrate>0:
        if nitrate>=10:
            print('dose 3ml')
        else:
            if nitrate>=2.5:
                print('dose 2ml')
            else:
                if nitrate>=1:
                    print('dose 1ml')
                else:
                    print('0.5ml')
