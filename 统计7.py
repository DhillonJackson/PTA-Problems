a=int(input())
list_print=[]
while a!=0:
    cnt=0
    for _ in range(a):
        n=int(input())
        if n%7==0 or n%10==7:
            cnt+=1
    list_print.append(cnt)
    a=int(input())
for i in list_print:
    print(i)