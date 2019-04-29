# 6、用户登陆（三次机会重试）
user = 'admin'
password = '123'
i = 0
while i < 3:
    name = input('please input usernmae:')
    pw = input('please input password:')
    if name == user and pw == password:
        print('login success')
    else:
        print('you have %d chance(s)'%(2-i))
        if (2-i) == 0:
            result = input('continue?yes')
            if result == 'yes':
                i = 0
                continue
    i += 1
else:
    print('login out of time')