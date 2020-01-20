m = input('what word do u want to remove')
x = ('the quick brown fox jumps over the lazy dog')
m2 = len(m)
m3 = x.find(m)
m4 = (m3-1)
m5 = (m3+m2)
left = x[0:m4]
right = x[m5:43]
print(left,right)
