intr = float(input('input intrest'))
bal = float(input('input balance'))
db = float(input('input desired balance'))
c = (1)
col = (':')
arr = ('-->')
while True:
    if bal!=db:
        x = (bal*intr)
        y = (bal+x)
        print("Year ",c,col,bal,arr,y)
        bal = (y)
        bal = round(bal,2)
        c = (c+1)
    if bal>db:
        break
    
