num=input()
lst=list(num)
newlist=[0,0,0,0,0,0,0,0,0,0]
for i in lst:
    temp=eval(i)
    newlist[temp]+=1
for i in range(10):
    if newlist[i]!=0:
        print(str(i)+':'+str(newlist[i]),end='\n')