#coding:utf-8
#学生信息管理系统
filename='student.txt'
import os
#主函数循环
def main():
    while True:
        menum()
        choice=int(input('请选择：'))
        if choice==0:    #当选择0时
            answer=input('您确定要退出系统吗？y/n\n')
            if answer=='y' or answer=='Y':     #输入y或Y退出系统
                print('感谢您的使用！')
                break
            else:         #当输入其他时，继续操作
                continue
        elif choice==1:
            insert()     #录入学生信息
        elif choice==2:
            search()     #查找学生信息
        elif choice==3:
            delete()     #删除学生信息
        elif choice==4:
            modify()     #修改学生信息
        elif choice==5:
            sort()       #排序
        elif choice==6:
            total()      #统计学生总人数
        elif choice==7:
            show()       #显示所有学生信息

#主菜单界面
def menum():
    print('========================================学生信管理息系统===========================================')
    print('--------------------------------------------功能菜单----------------------------------------------')
    print('\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t5.排序')
    print('\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t0.退出')
    print('-------------------------------------------------------------------------------------------------')

#录入学生信息
def insert():
    student_list=[]
    while True:
        id=input('请输入学号ID：')
        if not id:
            break
        name=input('请输入姓名：')
        if not name:
            break

        try:
            EnglishList=int(input('请输入英语成绩：'))
            ChineseList=int(input('请输入语文成绩：'))
            MathList=int(input('请输入数学成绩：'))
            ProfessionList=int(input('请输入专业成绩：'))
        except:
            print('输入无效，不是整数类型，请重新输入！')
            continue
        #将录入的学生信息保存到字典
        student={'id':id,'name':name,'English':EnglishList,'Chinese':ChineseList,'Math':MathList,'Profession':ProfessionList}
        #将学生信息添加到列表中
        student_list.append(student)
        answer=input('是否继续添加学生信息？y/n\n')
        if answer=='y' or answer=='Y':
            continue
        else:
            break
    
    #调用save()函数保存学生信息
    save(student_list)
    print('学生信息录入完毕！')

#将学生信息保存到student.txt文件中
def save(lst):
    try:
        stu_txt=open(filename,'a',encoding='utf-8')
    except:
        stu_txt=open(filename,'w',encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()

#查找学生信息
def search():
    student_query=[]
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            mode=input('按ID查找输入1，按姓名查找输入2：')
            if mode=='1':
                id=input('请输入学生学号：')
            elif mode=='2':
                name=input('请输入学生姓名：')
            else:
                print('输入有误请重新输入！')
                search()
            with open(filename,'r',encoding='utf-8') as sfile:
                student=sfile.readlines()
                for item in student:
                    d=dict(eval(item))
                    if id !='':
                        if d['id']==id:
                            student_query.append(d)
                    elif name !='':
                        if d['name']==name:
                            student_query.append(d)
            #显示查询结果
            show_student(student_query)
            #清空列表
            student_query.clear()
            answer=input('是否继续查询？y/n\n')
            if answer=='y' or answer=='Y':
                continue
            else:
                break
        else:
            print('未查到该学生信息！')
            return

#显示特定的学生列表
def show_student(lst):
    if len(lst)==0:
        print('未查到该学生信息！')
        return
    #定义标题显示格式
    format_title='{:^8}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}\t{:^8}'
    print('--------------------------------------------------------------------------------------------------')
    print(format_title.format('学号','姓名','英语成绩','语文成绩','数学成绩','专业成绩','总成绩'))
    #定义内容的显示格式
    format_data='{:^8}\t{:^12}\t{:^10}\t{:^10}\t{:^10}\t{:^8}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('English'),
                                 item.get('Chinese'),
                                 item.get('Math'),
                                 item.get('Profession'),
                                 int(item.get('English'))+int(item.get('Chinese'))+int(item.get('Math'))+int(item.get('Profession'))
                                 ))

#删除学生信eee
def delete():
    while True:
        student_id=input('请输入要删除的学生的学号ID：')
        if student_id != '':
            if os.path.exists(filename):   #若存在该学生，读取该学生的信息
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old=file.readlines()
            else:     #若不存在该学生，标记为空
                student_old=[]
            flag=False   #标记是否删除
            if student_old:
                with open(filename,'w',encoding='utf-8') as wfile:
                    d={}
                    for item in student_old:
                        d=dict(eval(item))    #将字符串转成字典
                        if d['id'] != student_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag=True
                    if flag:
                            print(f'学号为{student_id}的学生信息已被删除。')
                    else:
                            print(f'没有找到学号为{student_id}的学生信息。')
            else:
                print('无学生信息。')
                break
            show()     #删除之后重新显示所有学生的信息
            answer=input('是否继续删除？y/n\n')
            if answer=='y' or answer=='Y':
                continue
            else:
                break

#修改学生信息
def modify():
    #若文件存在
    if os.path.exists(filename):
        #读取文件中的学生列表，并将其保存在副本student_old中
        with open(filename,'r',encoding='utf-8') as mfile:
            student_old=mfile.readlines()
    #若文件不存在，退出修改
    else:
        return
    #查找要修改的学生
    student_id=input('请输入要修改的学生学号ID：')
    with open(filename,'w',encoding='utf-8') as wfile:
        #遍历学生列表，若存在该学生，进行修改
        for item in student_old:
            d=dict(eval(item))
            if d['id']==student_id:
                print('存在该学生，可以修改。')
                while True:
                    try:
                        d['name']=input('请输入姓名：')
                        d['English']=input('请输入英语成绩：')
                        d['Chinese']=input('请输入语文成绩：')
                        d['Math']=input('请输入数学成绩：')
                        d['Profession']=input('请输入专业成绩：')
                    except:
                        print('输入有误，请重新输入！')
                    else:
                        break
                #将修改后的学生列表进行拼接并写入文件中保存
                wfile.write(str(d)+'\n')
                print('修改成功！')
            else:
                wfile.write(str(d)+'\n')
        answer=input('是否继续修改？y/n\n')
        if answer=='y' or answer=='Y':
            modify()

#排序
def sort():
    student_list=[]
    #判断文件是否存在
    if os.path.exists(filename):
        #以只读方式打开文件
        with open(filename,'r',encoding='utf-8') as sofile:
            #将文件信息保存到学生列表中
            student_list=sofile.readlines()
        student_new=[]
        for item in student_list:
            d=dict(eval(item))
            student_new.append(d)
    else:
        return
    asc_or_desc=input('请选择（0，升序；1，降序）:')
    if asc_or_desc=='0':
        asc_or_desc_bool=False
    elif asc_or_desc=='1':
        asc_or_desc_bool=True
    else:
        print('您的输入有误，请重新输入！')
        sort()
    mode=input('请选择排序方式：1、按英语成绩；2、按语文成绩；3、按数学成绩；4、按专业成绩；5、按总成绩\n')
    if mode=='1':
        student_new.sort(key=lambda x:int(x['English']),reverse=asc_or_desc_bool)
    elif mode=='2':
        student_new.sort(key=lambda x:int(x['Chinese']),reverse=asc_or_desc_bool)
    elif mode=='3':
        student_new.sort(key=lambda x:int(x['Math']),reverse=asc_or_desc_bool)
    elif mode=='4':
        student_new.sort(key=lambda x:int(x['Profession']),reverse=asc_or_desc_bool)
    elif mode=='5':
        student_new.sort(key=lambda x:int(x['English'])+int(x['Chinese'])+int(x['Math'])+int(x['Profession']),reverse=asc_or_desc_bool)
    else:
        print('您的输入有误，请重新输入！')
        sort()
    show_student(student_new)

#统计学生总人数
def total():
    #若文件信息存在
    if os.path.exists(filename):
        #读取文件中的学生列表
        with open(filename,'r',encoding='utf-8') as tofile:
            students=tofile.readlines()
            if students:
                print(f'一共有{len(students)}名学生')
            else:
                print('还没有录入学生信息！')
    #若文件不存在
    else:
        print('暂未保存数据信息!')

#显示所有学生信息
def show():
    student_lst=[]
    #若文件存在，打开文件
    if os.path.exists(filename):
        #以只读方式打开文件
        with open(filename,'r',encoding='utf-8') as shfile:
            #将文件内容保存到students列表中
            students=shfile.readlines()
            #遍历students列表
            for item in students:
                #将学生信息转换成字典添加到学生列表中
                student_lst.append(eval(item))
            if student_lst:
                #若学生列表不为空，输出学生列表
                show_student(student_lst)
            #清空学生列表
            student_lst.clear()
    else:
        print('暂未保存数据！')

if __name__ == '__main__':
    main()