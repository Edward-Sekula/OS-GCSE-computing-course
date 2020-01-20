div = int(input('divide by'))
num = int(input('input your number'))
g = (num/div)
f = (num%div)
if f==0:
    print(num, ' is exactly divisible by your number', g)
else:
    print(f)
