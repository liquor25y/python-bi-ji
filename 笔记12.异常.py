#处理数字不能除以0的异常
print(5/0)
#traceback: ZeroDivisionError: division by zero
#我们可以根据信息对该种程序进行修改，告诉python发生错误时如何应对

#1.使用try_except代码模块(只能在当前这一小段中使用)
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

#2.else代码块
#制作一个只执行除法运算的简单计算机
print("Give me two numbers,and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number=input("\nFirst number:")
    if first_number == 'q':
        break
    second_number =input("\nSecond number:")
    if second_number=='q':
        break
    answer=int(first_number)/int(second_number)
    print(answer)
#上述代码不能处理5/0的情况
#需要添加一个else模块
print("Give me two numbers,and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number=input("\nFirst number:")
    if first_number == 'q':
        print("successfully quit")
        break
    second_number =input("\nSecond number:")
    if second_number=='q':
        print("successfully quit")
        break
    try:
        answer=int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)

#3.处理FileNotFoundError异常
filename='alice.txt'
with open(filename,encoding='utf-8') as f:#encoding:读入时能够读中文
    contents=f.read()#其实执行时将找不到该文件

#修改
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, there is no {filename} here")

#4.分析文本split
title="Alice in Wonderland"
title.split()
print(title.split())#将字符串变成一个含有三个元素的列表

#5.使用多个文件(通过for循环)
filenames=['alice.txt','little_women.txt']
for filename in filenames:
    #--snip--

#6.静默失败
#不一定每次不可执行都要有反应 可以默认跳过
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    pass#这样找不到直接就不反应

#7.存储数据 json.dump()和json.load()
import  json#模块json可以将简单的数据结构转储到文件当中
numbers=[2,3,5,7,11,13]

filename='numbers.json'#通常用文件拓展名为json的文件记录下数据
with open(filename,'w') as f:
    json.dump(numbers,f)#dump将numbers存储在f当中

import json
filename='numbers.json'
with open(filename) as f:
    numbers1=json.load(f)#加载出存储在numbers.json中的信息
print(numbers1)

#8.保存和读取用户生成的数据
#提示用户首次运行时输入自己的名字，并在再次运行程序时记住他
import json
username=input("What is your name?")
filename='username.json'
with open (filename,'w') as f:
    json.dump(username,f)
    print(f"We'll remember you when you come back,{username}! ")

#再编写一个程序 向已经存储了名字的用户发出问候
import json
filename='username.json'
with open(filename) as f:
    username=json.load(f)
    print(f"Welcome back,{username}!")

#将两个代码整合到一起 能够提示用户输入用户名
import json
filename='username.json'
try:
    with open(filename) as f:
        username=json.load(f)
except FileNotFoundError:
    username=input("What is your name?")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back,{username}! ")
else:
    print(f"Welcome back,{username}!")

#9.重构(将上述代码修改使总体明确)（优化，使数据内容更加清晰）
import json
def get_sorted_username():
    filename='username.json'
    try:
        with open(filename) as f:
            username=json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What is your name?")
    filename='username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    username=get_sorted_username()#调用先前定义的函数
    if username:
        print(f"Welcome back,{username}!")
    else:
        username =get_sorted_username()#调用上面新增
        print(f"We'll remember you when you come back,{username}! ")
greet_user()
