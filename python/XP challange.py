print('enter xp')
xp = (0)
rank = (1)
rankn = ('private')
while True:
    y = int(input())
    xp = (xp+y)
    if xp>100 and rank == 1:
        rank = (rank+1)
        rankn = (' Corpral')
        print('New Rank! ',rank,rankn)
        xp = (xp-100)
        print(xp,'xp carried over')
    if xp>300 and rank == 2:
        rank = (rank+1)
        rankn = (' Sergeant')
        print('New Rank! ',rank,rankn)
        xp = (xp-100)
        print(xp,'xp carried over')
    else:
        print(xp)
        print(rankn)
        
        
        
