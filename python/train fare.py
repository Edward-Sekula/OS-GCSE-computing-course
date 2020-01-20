sta = int(input('how many stations are you passing through today?'))
ad = int(input('how many adults are traveling with you'))
ch = int(input('how many children are traveling with you'))
ti = int(input('what time is it'))

bf = ((ad*sta*20)+(ch*sta*10))

#time
if 6<=ti<=9:
    bfaread = (ad*25)
    faread = (bfaread*sta)
    farech = (((25/2)*ch)*sta)
    fare = (farech+faread)
    print('£',fare)
else:
    bf = ((ad*sta*20)+(ch*sta*10))
    print('£',bf)
