n=int(input())
dicta={'J':0,'B':0,'C':0}
dictb={'J':0,'B':0,'C':0}
lista=[0,0,0]
listb=[0,0,0]  #注意是胜、平、负的次序
for i in range(n):
    a,b=input().split()
    if a=='J' and b=='B':
        lista[0]+=1
        dicta['J']+=1
    elif a=='B' and b=='C':
        lista[0]+=1
        dicta['B']+=1
    elif a=='C' and b=='J':
        lista[0]+=1
        dicta['C']+=1
    elif a==b:
        lista[1]+=1
    elif a=='J':
        dictb['C']+=1
    elif a=='B':
        dictb['J']+=1
    elif a=='C':
        dictb['B']+=1
lista[2]=n-lista[0]-lista[1]
listb[0]=lista[2]
listb[1]=lista[1]
listb[2]=lista[0]
#字典不能直接转化为列表，怎么办呢？  同时希望能够使用sort排序  -ord()的想法很好  因为对于数字而言，希望reverse=True,而对于字母，又希望reverse=False
listaa=[('J',dicta['J']),('B',dicta['B']),('C',dicta['C'])]
listbb=[('J',dictb['J']),('B',dictb['B']),('C',dictb['C'])]
listaa.sort(key= lambda x:(x[1],-ord(x[0])),reverse=True)  #注意这个新学到的写法
listbb.sort(key= lambda x:(x[1],-ord(x[0])),reverse=True)  
#注意打印格式的问题！！！  
'''
for i in range(3):
    print(lista[i],end=' ')
print('')
for i in range(3):
    print(listb[i],end=' ')
print('')
'''
#如果按照以上这种方式打印，每一行最后一个数字后面都会有一个空格，而且需要手动打印换行
print(lista[0],lista[1],lista[2])
print(listb[0],listb[1],listb[2])

print(listaa[0][0],listbb[0][0])

'''
满分答案：
a = int(input())
x1=y1=z1=0
x2=y2=z2=0
e=0
for i in range(a):
    x = input().split()
    if x[0]=='B' and x[1]=='C':
        x1+=1
    elif x[0]=='C' and x[1]=='J':
        y1+=1
    elif x[0]=='J' and x[1]=='B':
        z1+=1
    elif x[0]=='C' and x[1]=='B':
        x2+=1
    elif x[0]=='J' and x[1]=='C':
        y2+=1
    elif x[0]=='B' and x[1]=='J':
        z2+=1
    else:
        e+=1
print(x1+y1+z1,e,a-x1-y1-z1-e)
print(x2+y2+z2,e,a-x2-y2-z2-e)
if x1>=y1 and x1>=z1:
    s = 'B'
elif y1>x1 and y1>=z1:
    s = 'C'
else:
    s = 'J'
if x2>=y2 and x2>=z2:
    s2 = 'B'
elif y2>x2 and y2>=z2:
    s2 = 'C'
else:
    s2 = 'J'
print(s,s2)
'''