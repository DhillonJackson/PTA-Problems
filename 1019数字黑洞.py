#终于过了woc
'''写一下对这道题的一些思考：
警惕输入的时候数字位数不满四位  以及
'''
n=list(input().rjust(4,'0'))
list1=sorted(n,reverse=True)
list2=sorted(n,reverse=False)
num1=''.join(list1)
num2=''.join(list2)
while int(num1)-int(num2)!=6174 and num1!=num2:
    print(num1+' - '+num2+' = {0}'.format(str(int(num1)-int(num2)).rjust(4,'0')))
    n=list(str(int(num1)-int(num2)).rjust(4,'0'))
    list1=sorted(n,reverse=True)
    list2=sorted(n,reverse=False)
    num1=''.join(list1)
    num2=''.join(list2)
if num1!=num2:
    print(num1+' - '+num2+' = 6174')
else:
    print(num1+' - '+num2+' = 0000')
#验证程序  即验证在运算过程中不会出现四位数字相等：
'''
for i in range(10000):
    n=list(str(i).rjust(4,'0'))
    list1=sorted(n,reverse=True)
    list2=sorted(n,reverse=False)
    num1=''.join(list1)
    num2=''.join(list2)
    while int(num1)-int(num2)!=6174 and num1!=num2:
        #print(num1+' - '+num2+' = {0}'.format(str(int(num1)-int(num2)).rjust(4,'0')))
        n=list(str(int(num1)-int(num2)).rjust(4,'0'))
        list1=sorted(n,reverse=True)
        list2=sorted(n,reverse=False)
        num1=''.join(list1)
        num2=''.join(list2)
    if num1==num2:
        print(str(i).rjust(4,'0'))
print('completed')
'''

'''n=list(input())
numlist=[]
for i in n:
    numlist.append(int(i))
list1=sorted(numlist,reverse=True)
strlist1=[str(i) for i in list1]
str1=''.join(strlist1)
list2=sorted(numlist,reverse=False)
strlist2=[str(i) for i in list2]
str2=''.join(strlist2)
num1=list1[0]*1000+list1[1]*100+list1[2]*10+list1[3]*1
num2=list2[0]*1000+list2[1]*100+list2[2]*10+list2[3]*1
if num1-num2==6174:
    print('{0} - {1} = {2}'.format(str1,str2,num1-num2))
elif num1==num2:
    print('{0} - {1} = 0000'.format(str1,str2))
else:
    while num1-num2!=6174:
        print('{0} - {1} = {2}'.format(str1,str2,num1-num2))
        n=list(str(num1-num2))
        numlist=[]
        for i in n:
            numlist.append(int(i))
        list1=sorted(numlist,reverse=True)
        strlist1=[str(i) for i in list1]
        str1=''.join(strlist1)
        list2=sorted(numlist,reverse=False)
        strlist2=[str(i) for i in list2]
        str2=''.join(strlist2)
        num1=list1[0]*1000+list1[1]*100+list1[2]*10+list1[3]*1
        num2=list2[0]*1000+list2[1]*100+list2[2]*10+list2[3]*1
    print('{0} - {1} = {2}'.format(num1,num2,num1-num2))
''' 
'''
'''
#第二版
'''n=list(input().rjust(4,'0'))
list1=sorted(n,reverse=True)
list2=sorted(n,reverse=False)
num1=''.join(list1)
num2=''.join(list2)
if num1==num2:
    print(num1+' - '+num2+' = 0000')

else:
    while int(num1)-int(num2)!=6174:
        print(num1+' - '+num2+' = {0}'.format(int(num1)-int(num2)))
        n=list(str(int(num1)-int(num2)))
        list1=sorted(n,reverse=True)
        list2=sorted(n,reverse=False)
        num1=''.join(list1)
        num2=''.join(list2)
    print(num1+' - '+num2+' = 6174')'''
#满分版
'''
#输入数字，若不足4位，则使用rjust在左侧用0补全至4位
n=input().rjust(4,'0')
 
#如果四位都相同，则直接输出
if n[0]==n[1]==n[2]==n[3]:
    print(n+' - '+n+' = 0000')
else:
    #循环按要求进行计算，知道n为6174再跳出循环
    while True:
        #将字符串转换为列表，经过排序后再重新转换为字符串
        n_1=''.join(sorted(list(n)))
        #进行对应的计算，如果结果不足4位要用0补全
        n=str(int(n_1[::-1])-int(n_1)).rjust(4,'0')
        #按规定格式输出
        print('%s - %s = %s'%(n_1[::-1],n_1,n))
        if n=='6174':
            break'''
