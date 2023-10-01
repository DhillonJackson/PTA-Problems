def gcd(m,n):
    if m%n==0:
        return n
    else:
        return gcd(n,m%n)

def minmultiple(m,n):
    a=min(m,n)
    b=max(m,n)
    if b%a==0:
        return b
    else:
        temp=b
        while b%a!=0:
            b+=temp
        return b
a,b=map(int,input().split())
if a*b==gcd(a,b)*minmultiple(a,b):
    print('Yes')
