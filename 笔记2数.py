#整数 浮点数
1+2.0##得3.0，无论什么运算，操作有浮点数，结果都是浮点数

#2.数字中得下划线 当数字很大时，可以用下划线将数字分组
universe_age=14_000_000_000
#出来不会包含下划线
print(universe_age)

#3.给多个变量赋值
x,y,z=0,0,0

#4.常量
#常量类似于变量，在程序得生命周期中保持不变，python内没有内置常量类别，《python程序员习惯使用全大写将某个变量应用为常量》
MAX_CONNECTIONS=500

print(MAX_CONNECTIONS)
MAX_CONNECTIONS=3#还是能赋值得，只是一个习惯


