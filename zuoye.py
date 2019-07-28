'''
# 1. 输入三条边的长度如果能构成三角形就计算周长和面积
a=float(input("请输入一条边长a："))
b=float(input("请输入一条边长b："))
c=float(input("请输入一条边长c："))

if (a+b>c and a+c>b and b+c>a):
    p = a+b+c
    s = (a+b+c)/2 
    area = (s*(s-a)*(s-b)*(s-c))**0.5 
    print("三角形周长为：%0.2f" %p, "三角形面积为 :%0.2f" %(area))
else :
    print ("不能构成三角形")

'''

a= str (input("请输入用户名："))
b= str (input("请输入密码："))

if a[0] in ["0","1","2","3","4","5","6","7","8","9"]:
    print ("访问失败")
elif a=="方开":
    if b==123:
        print("管理员登录成功")
    else:
        print("密码错误")
elif a=="刘晨":
    if b==12345:
        print("管理员登录成功")
    else:
        print("密码错误")
elif a=="张旭":
    if b==123321:
        print("用户登录成功")
    else:
        print("密码错误")
elif a=="沈章":
    if b==123456:
        print("用户登录成功")
    else:
        print("密码错误")
elif a=="许景":
    if b==123456:
        print("用户登录成功")
    else:
        print("密码错误")
elif a not in ("方开","刘晨","张旭","沈章","许景"):
    if b== "guset":
        print("访客登录成功")
    else:
        print("密码错误")
else:
    print ("用户不存在")

    
