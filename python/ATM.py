
bal = (1000)
req = int(input('how much money do u want to take out'))
print('notes availiable: £10, £20')
if req>250:
    print('you have gone over the valid amount')
else:
    if req>bal:
        print('request exceedes balance')
    else:
        if req%10!=0:
            print('request not divisible by 10')
        if req%10 == 0:
            t20 = (req//20)
            rem = (req%20)
            t10 = int(rem/10)
            print(t20,' £20 notes ','and ',t10,' £10 notes')
            bal = (bal-req)
    


    




