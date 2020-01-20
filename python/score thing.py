score = int(input('what is the score'))
if score<40:
    print('FAIL')
if score>40:
    if score<60:
        print('pass')
    if score>=60:
        if score<80:
            print('merit')
        if score>=80:
            print('distinction')
