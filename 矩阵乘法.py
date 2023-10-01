a,b=map(int,input().split(' '))    #a为行数，b为列数
lst1=[]
for i in range(a):
    newlst=map(int,input().split(' '))
    newlist=list(newlst)
    lst1.append(newlist)

#以上是第一个矩阵
c,d=map(int,input().split(' '))    #c为行数，d为列数
lst2=[]
for i in range(c):
    newlst=map(int,input().split(' '))
    newlist=list(newlst)
    lst2.append(newlist)
#以上是第二个矩阵
product=[] #储存乘积结果
product2=[]
result=0
for i in range(a):
    for j in range(d):
        for k in range(b):
            result+=lst1[i][k]*lst2[k][j]
        product.append(result)
        result=0
    product2.append(product)
    product=[]
#打印
#打印输入矩阵1
for i in range(a):
    print(lst1[i],end='\n')
for i in range(c):
    print(lst2[i],end='\n')
#打印乘积矩阵
for i in range(a):
    print(product2[i],end='\n')