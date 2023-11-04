import math
num1 = int(input())
lis =[]
for i in range(num1):
    num = int(input())
    lis.append(num)
for item in  lis:
    x = math.sqrt(item)
    b = int(x * 10000)/10000
    print('%.4f'% b)
    