#整数重组
def weishu(n):
    cnt=0
    while n!=0:
        n//=10
        cnt+=1
    return cnt

a=int(input('请输入第一个整数：'))
b=int(input('请输入第二个整数：'))
#位数
k=weishu(a)
num1=a%pow(10,k-b+1)
num2=a%pow(10,k-b)
num3=(a//pow(10,k-b))%10
num4=num2*10+num3
res=a-num1+num4
print(res)