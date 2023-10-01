year=int(input('请输入查询年份：'))
month=int(input('请输入查询月份：'))
def judge(n):
    cnt=0
    for i in range(1,n):
        if i%400==0 or (i%4==0 and i%100!=0) :
            cnt+=1
    return cnt
day=366*judge(year)+365*(year-judge(year)-1)
def center(year,month):
    str="{0}--{1}".format(year,month)
    print(str.center(49))
#准备工作
center(year,month)
print('1\t2\t3\t4\t5\t6\t7\t')

if year%400==0 or (year%4==0 and year%100!=0) :
    Feb=29  #闰年二月TM是29天
else:
    Feb=28
lst=[0,31,Feb,31,30,31,30,31,31,30,31,30,31]
day2=0
for i in range(month):
    day2+=lst[i]
Day=day+day2
pre=Day%7
for i in range(pre):
    print('\t',end='')
count=pre
need=lst[month]
for i in range(1,need+1):
    count+=1
    if count%7==0:
        print(i)
    else:
        print(i,end='\t')
