hrs = int(input('how many hours have you worked this week'))
hr = int(input('what is your hourly rate'))
if 0<hrs<=60:
    if hrs>40:
        ot = (hrs-40)
        otr = (hr*(3/2))
        s40 = (40*hr)
        sot = (ot*otr)
        sal = (sot+s40)
        print('salary is $',sal)
    elif hrs<=40:
        print('salary is $'(hrs*hr))

else:
    print('error')
