'''lst=[1,5,3,8,9,7,0,-9,-7]
for _ in range(8):
    for i in range(8-_):
        if(lst[i]>lst[i+1]) :
            lst[i],lst[i+1]=lst[i+1],lst[i]

print(lst)'''
#根据需要创建列表
n=int(input('请输入列表元素个数：'))
lst=[]
for i in range(n):
    a=int(input())
    lst.append(a)
print(lst)
#排序
lst.sort()
print(lst)#升序排列
lst.sort(reverse=True)
print(lst)#降序排列
lst.sort(reverse=False)
print(lst)#升序排列