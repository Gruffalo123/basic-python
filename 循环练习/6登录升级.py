# 登录验证（三次机会）升级版
username = 'admin'
password = '123'
i = 3
while i > 0:
    i = i-1
    name = input('请输入用户名：')
    if name == username:
        pw = input('请输入密码：')
        if pw == password:
            print('验证成功！正在登录...请稍候')
            break
        else:
            print('您的密码有误，请重新输入！')
            print('您还有%s次机会' % (i))
        if i == 0:
            print('今日次数已用完')
            chance = input('是否还想再次尝试？Y(不区分大小写)')
            if chance.upper() == 'Y':
                i = 3
                continue
    else:
        print('用户名不存在，请重新输入：')
        print('您还有%s次机会' % (i))
        if i == 0:
            print('今日次数已用完')
            chance = input('是否还想再次尝试？Y(不区分大小写)')
            if chance.upper() == 'Y':
                i = 3
                continue
else:
    print('看来是无法登录了，快去想想怎么解决吧!')