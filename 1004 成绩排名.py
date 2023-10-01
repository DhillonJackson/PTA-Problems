a=int(input())
lstsum=[]
lstmax=[]
for i in range(a):
    d,b,c=input().split()
    lst=[d,b,c]
    lstmax.append(int(c))
    lstsum.append(lst)
maxi=max(lstmax)
count=0
for i in range(a):
    if lstmax[i]==maxi:
        count=i
        break
mini=min(lstmax)
cnt=0
for i in range(a):
    if lstmax[i]==mini:
        cnt=i
        break
print(lstsum[count][0],lstsum[count][1])
print(lstsum[cnt][0],lstsum[cnt][1])