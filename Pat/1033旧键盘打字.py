# Python upper() 方法将字符串中的小写字母转为大写字母。
def judge(num_2):
    if num_2.isupper() and flag:        #判断字符：如果是大写则不输出   并且 flag 为 0  -》表示 没 “+” 存在
        return False
    elif num_2.upper() in bad_str:       #判断：若字符的大写在 ... 中   返回  错误
        return False
    else:
        return True

bad_str,my_str = input(),input()
flag = 0
for num_1 in bad_str:        #  "+"  为  上档键   上档键  坏掉  则 大写 英文字母 无法 被 打出
    if num_1 == '+':
        flag = 1

for num_2 in my_str:
    if judge(num_2):           #  符合条件 则输出
        print(num_2,end="")
