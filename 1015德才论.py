import sys
N, L, H = map(int, sys.stdin.readline().split())
num1 = []
num2 = []
num3 = []
num4 = []
 

def printf(num):
    if num:
        for i in num:
            print("%d %d %d" % (i[0], i[1], i[2]))
 
 
for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    if temp[1] >= L and temp[2] >= L:
        if temp[1] >= H and temp[2] >= H:
            num1.append(temp)
        elif temp[1] >= H and temp[2] < H:
            num2.append(temp)
        elif temp[1] >= temp[2]:
            num3.append(temp)
        else:
            num4.append(temp)
num1.sort(key=lambda x: (-(x[1] + x[2]), -x[1], x[0]))  #核心  这个相同比较下个  下一个若相同则比较再下一个
num2.sort(key=lambda x: (-(x[1] + x[2]), -x[1], x[0]))  #关注lambda函数的写法
num3.sort(key=lambda x: (-(x[1] + x[2]), -x[1], x[0]))
num4.sort(key=lambda x: (-(x[1] + x[2]), -x[1], x[0]))
print(len(num1) + len(num2) + len(num3) + len(num4))
printf(num1)
printf(num2)
printf(num3)
printf(num4)