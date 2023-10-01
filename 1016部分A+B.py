a,b,c,d=input().split()
lst1=[]
lst2=[]
for i in a:
    if i==b:
        lst1.append(i)
if bool(lst1)==True:
    int1=''.join(lst1)
else:
    int1=0
for i in c:
    if i==d:
        lst2.append(i)
if bool(lst2)==True:
    int2=''.join(lst2)
else:
    int2=0
print(int(int1)+int(int2))