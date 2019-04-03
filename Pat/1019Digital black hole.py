def hei(a):
    x = sorted(a,reverse = True)
    y = sorted(a)
    str1 = ''
    str2 = ''
    for i in x:
        str1+=i
    for i in y:
        str2+=i
    result = str(int(str1)-int(str2))
    if len(result)<4:
        result = '0'*(4-len(result))+result
    if result=='0000':
        print('%s %s %s %s %s'%(str1,'-',str2,'=','0000'))
    else:
        print('%s %s %s %s %s'%(str1,'-',str2,'=',result))
    return result
a = input()
if len(a)<4:
    a+='0'*(4-len(a))
str1 = hei(a)
while (str1!='0000'):
    if str1 == '6174' or str1 == '0':
        break
    str1 = hei(str1)

