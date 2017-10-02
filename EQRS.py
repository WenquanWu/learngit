import sys
class EQRS:
        def  add():
            import Re
            n=input("请输入该生学号:")
            s=input("请输入该生成绩:")
            Re.Results[n]=s
        def  dels():
            n=input("请输入该生学号:")
            import Re
            del  Re.Results[n]
            print ('已成功删除，请重新输入该生成绩')
        def  inquire():
            import Re
            print ('1->查询  2->退出')
            n=input('请选择:')
            if  n=='1':
                nu=input("请输入该生学号:")
                s=Re.Results[nu]
                print('该生成绩为:',s)
            else:
               pass
        def  showall():
            import Re
            s=Re.Results.items()
            print(s)
        def  test():
            print('1->录入  2->查询  3->删除  4->查看')
            t=input("选择:")
            if t=='1':
                print ('成绩录入(请输入01--10学生成绩，初始化默认为60)')
                EQRS.add()
            elif t=='2':
                 print ('成绩查询')
                 EQRS.inquire()
            elif t=='3':
                print ('成绩删除')
                EQRS.dels()
            else:
                EQRS.showall()
while True:
    EQRS.test()
