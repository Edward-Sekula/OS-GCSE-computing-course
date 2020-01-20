temp = int(input('what temp is the water'))
if temp<=0:
    print('frozen')
if temp>0:
    if temp<100:
        print('neither')
    if temp>100:
        print('boiling')
