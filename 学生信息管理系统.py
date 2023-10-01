#学生信息管理系统
def main():
    print('--------------------学生信息管理系统-----------------------')
    print('1.添加')
    print('2.删除')
    print('3.修改')
    print('4.展示')
    print('5.寻找')
    print('6.排序')
def add(studentlist):
    id=int(input('请输入学号：'))
    flag=0
    for i in studentlist:
        if i.get('id')==id:
            flag=1
            break
    if flag==1:
        print('该学生信息已存在，无法添加')
    else :
        with open(r'D:\Python\程序代码\学生信息管理系统写入数据.txt','w+',encoding='gbk') as file:
            file.write(str(id))
            file.write('\n')
            name=input('请输入姓名：')
            file.write(name)
            file.write('\n')
            score=int(input('请输入成绩：'))
            file.write(str(score))
            file.write('\n')
        dic={'id':id,'name':name,'score':score}
        studentlist.append(dic)
        print('学生信息添加成功')

def delete(studentlist):
    id=int(input('请输入学号：'))
    flag=0
    for i in studentlist:
        if i.get('id')==id:
            studentlist.remove(i)
            flag=1
            print('学生信息删除成功')
    if flag==0:
        print('学生信息不存在')
    

def update(studentlist):
    id=int(input('请输入学号：'))
    flag=0
    for i in studentlist:
        if i.get('id')==id:
            score=int(input('请输入要更改的成绩'))
            i['score']=score
            flag=1
            print('学生信息更新成功')
    if flag==0:
        print('学生信息不存在')
def show(studentlist):
    for i in studentlist:
        print(i.get('id'),'\t\t',i.get('name'),'\t\t',str(i.get('score')))
def find(studentlist):
    pass
def sort(studentlist):
    #冒泡排序
    len=studentlist.__len__()
    for i in range(1,len):
        for k in range(len-i):
            if studentlist[k].get('score')>studentlist[k+1].get('score'):
                studentlist[k],studentlist[k+1]=studentlist[k+1],studentlist[k]
studentlist=[]
while True:
    a=int(input('请输入操作指令：'))
    if a==1:
        add(studentlist)
        show(studentlist)
    elif a==2:
        delete(studentlist)
        show(studentlist)
    elif a==3:
        update(studentlist)
        show(studentlist)
    elif a==4:
        show(studentlist)
    elif a==5:
        find(studentlist)
        show(studentlist)
    elif a==6:
        sort(studentlist)
        show(studentlist)
    b=input('请问是否退出系统？ 您可以输入Y退出系统,或输入N继续进行操作：')
    if b=='Y':
        break
    else :
        continue
print('感谢您的使用，我们下次再会！')