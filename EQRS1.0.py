Results={'01':60}
class EQRS:


    def add():
        n=input('请输入该生学号:')
        s=input('请输入该生成绩:')
        Results[n]=s

    def inquire():
        print('1>-查询  2->退出')
        n=input('请选择:')
        if n=='1':
            t=input('请输入该生学号:')
            if t in Results.keys():
                print('该生成绩为:',Results[t])
            else:
                print('该学生未录入成绩,请选择4查看')
        elif n=='2':
            pass
        else:
            print('输入错误，请重试')

    def dels():
        n=input('请输入该生学号:')
        del Results[n]
        print ('已成功删除，请重新输入该生成绩')
        Results[n]=input('该生新成绩为:')

    def showall():
        print('打印成绩单如下')
        for i in Results.keys():
            print('学号:',i,'  成绩:',Results[i])

    def test():
        print('1->录入  2->查询  3->删除  4->查看   (备注:学号输入格式为01--99)')
        t=input('请选择:')
        if t=='1':
            print('成绩录入(默认初始成绩为60)')
            EQRS.add()
        elif t=='2':
            print ('成绩查询')
            EQRS.inquire()
        elif t=='3':
            print ('成绩删除')
            EQRS.dels()
        elif t=='4':
            EQRS.showall()
        else:
            print('输入错误，请重试')


while True:
    EQRS.test()
        
