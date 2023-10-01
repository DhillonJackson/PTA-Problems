#学生信息管理系统
'''n=int(input('请输入学生人数个数：'))
lst=[]
for i in range(n):
    temp=dict({'姓名':input('请输入学生姓名：'),'学号':int(input('请输入学号：')),'成绩':int(input('请输入成绩：'))})
    lst.append(temp)
for i in range(n):
    print(lst[i])

lst[0]['姓名']='马名乐'
for i in range(n):
    print(lst[i])'''

'''def sort(lst,n):
    for _ in range(n):
        for i in range(n-_-1):
            if(lst[i]>lst[i+1]) :
                lst[i],lst[i+1]=lst[i+1],lst[i]

lst=[8,7,6,5,4,3,2,1]
sort(lst,8)
print(lst)'''

'''def fun(a,b) :
    a=15
    b['score']=98

a=12
b={'lisi':99}
fun(a,b)
print(a)
print(b)'''

'''def printf(lst) :
    lst1=[]
    lst2=[]
    for i in lst:
        if i%2==0:
            lst1.append(i)
        else :
            lst2.append(i)
    
    return lst1,lst2


lst=[1,2,3,4,5,6]
c=printf(lst)
print(c)'''
'''def fun(a,b=4):
    print(a,b)
fun(20,30)'''


'''def fib(n) :
    if n==1 or n==2:
        return 1
    else :
        return fib(n-1)+fib(n-2)

n=int(input('请输入数列项数：'))
print(fib(n))'''
'''def fun(*args):
    print(args)
    #print()

lst1=[1,2,3]
lst2=[4,5,6]
fun(lst1,lst2)'''
'''def fun(*argc,**argv):
    print(argc)
    print(argv)
    a=(argc,argv) #元组可各种数据混存
    print(a)
fun(1,2,3,a=4,b=5)'''

'''def fun(a,b,c):
    print(a)
    print(b)
    print(c)
fun(a=1,c=2,b=3)'''
#def fun(a,b,*,c,d):
'''def fun(*,c,d,**a):
    print(c,d,a)
fun(c=1,d=2,e=9)'''
#递归阶乘
'''def fac(n):
    if n==1 or n==0:
        return n
    else :
        return n*fac(n-1)
print(fac())'''
'''def fun (**argv):
    print(argv)
fun(a=1)'''
'''a={1,2,3,4,5,6}
b=(7,8,9)
a.update(b)
print(a)'''
'''for i in range(3):
    password=input('请输入密码：')
    if password=='admin':
        print('密码正确')
        break
    else :
        print('密码错误')
else :
    print('Sorry,you have mistaken the password for three times,you fucing asshole!')'''
#print('abc'.join('def'))
'''import math
def sushu(n):
    a=math.sqrt(n)
    for i in range(2,int(a)+1):
        if n%i==0:
            return 0  #非素数返回0
            break
    else :
        return 1 #素数返回1
print(sushu(1))'''
'''for i in range(2,0):
    print(i)'''
'''import math
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
print(cnt)'''
'''#include<stdio.h>
#include<math.h>
int sushu(int n)
{
    int i;
    for(i=2;i<=sqrt(n);i++) {
        if(n%i==0) break;
    }
    if(i>sqrt(n)) return 0;
    else return 1;
    
}
int main()
{
    int n,i,k=1,count=0,j;
    scanf("%d",&n);
    int a[1000000];
    a[0]=0;
    for(i=2;i<=n;i++) {
        if(sushu(i)==0) {
            a[k]=i;
            k++;
        }
    }
    for(j=1;j<=k-2;j++) {
        if(a[j+1]-a[j]==2) count++;
    }
    printf("%d",count);
    return 0;
}'''
'''import math
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
print(cnt)'''
'''dic={'lisi':99,'wnsd':45}
for i in dic:
    print(i)'''

'''try:
    a=int(input())
    b=int(input())                #try-except   BaseException
    print(a/b)
except ZeroDivisionError:
    print(0)
except BaseException as e:
    print(e)'''
'''try:
    a=int(input())
    b=int(input())                #try-except   BaseException
    print(a/b)
except:
    print('no')'''
'''import traceback
try:
    a=int(input())
    b=int(input())                #try-except   BaseException
    print(a/b)
except:
    traceback.print_exc()'''#导入traceback模块
'''class Dog(object): #很像 C 结构体
    name='李四'
    def __init__(self,name,age):
        print('汪汪汪')
        print(name,age)
        self.name=name
        self.age=age
    @staticmethod
    def static():
        print('我是static')
    @classmethod
    def classmethod(cls):
        print('我是类方法')
    def shili(self):

        print('我是实例方法')
    def example(self):
        print(self.name,self.age())
    class A:
    def __init__(self,name,age) -> None:
        print(name,age,'我是父类')
    
    def method(self):
        print('我是类方法')
class boy(A):
    def __init__(self, name, age) -> None:
        #super().__init__(name, age)
        print(1)
    
   
a=boy('lisi',13)
a.method()
'''
'''class stu:
    def __init__(self) -> None:
        print('hello')
    def __str__(self):
        super().__str__()
        print('我是__str__()方法')
a=stu()
b=a.__str__()
print(b)'''


lst=[[1,2,3],[4,5,98],[56,12,22]]
lst.sort(key=lambda lam:lam[2],reverse=True)
print(lst)