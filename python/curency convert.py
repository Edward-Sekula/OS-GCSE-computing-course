print('1.USD to GBP\n2.GBP to USD')
x = int(input())
c = ['GBP-USD','1.28','USD-GBP','0.883']
def USDGBP():
    y = int(input('input $ amount'))
    ug = float(c[3])
    z = y*ug
    print('a rate 1$ to ',c[3],'£ your money would equal ',z,'GBP')
def GBPUSD():
    y = int(input('input $ amount'))
    ug = float(c[1])
    z = y*ug
    print('a rate 1£ to ',c[1],'$ your money would equal ',z,'USD')   
if x == 1:
    USDGBP()
if x == 2:
    GBPUSD()
    
