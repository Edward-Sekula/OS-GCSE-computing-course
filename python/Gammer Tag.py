print('input GT(must be below 15 charachters)')
while True:
    x = input()
    y = len(x)
    if y<=15:
        print('GT accepted')
        break
    if y>15:
        print('try again')
        
