word = input()
f = len(word)
count = (0)
score = (0)
for k in range(f):
    x = (word[count])
    car = 'eariotnslcudpmhgbfywkvxzjq'
    m3 = car.find(x)
    point = (m3+1)
    score = (score + point)
    count = (count+1)
print(score)
