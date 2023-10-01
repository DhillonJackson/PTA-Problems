import math
def sushu(n):
    a=math.sqrt(n)
    for i in range(2,int(a)+1):
        if n%i==0:
            return 0  #非素数返回0
            break
    else :
        return 1 #素数返回1
n=int(input())
cnt=0
count=0
lst=[]
for i in range(2,n+1):
    if sushu(i)==1:
        lst.append(i)
        count+=1
for i in range(1,count):
    if lst[i]-lst[i-1]==2:
        cnt+=1
print(cnt)