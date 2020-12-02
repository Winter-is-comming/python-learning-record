import aoj

#在下面填入帐号密码和sckey
user_id = ['帐号1', '帐号2']
password = ['密码1', '密码2']
sckey = ['sckey1',
         'sckey2']


#如果不部署到阿里云函数计算上，就把第15到16行去掉，再把第10,11行的井号去掉
# for i in range(len(user_id)):
#     aoj.sign(user_id[i], password[i], sckey[i])


def main():
    for i in range(len(user_id)):
        aoj.sign(user_id[i], password[i], sckey[i])
