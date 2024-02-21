#1.输入函数input()让程序暂停，等待用户输入一些文本
message=input("Tell me something,and I will repeat it back to you:")
print(message)

print(f"\nyou input{message}")

#2.当需要输入的东西过长，可以拼凑,代换
prompt="If you tell us who you are,we can personalize the message you see."
prompt+="\n What is your first name?"
name=input(prompt)

#3.使用int()来获取数值输入
age=input("How old arw you?")
age#输出的值为'19'(字符串)，不能作为数字和别的数字比较，int()可以将其变换成为数值
age=int(age)#变成了数字
age >= 18

#4.求模运算符%
6%3

#5.while循环
current_number=1
while current_number <=5:
    print(current_number)
    current_number+=1

#6.让用户选择何时退出
prompt="\nTell me something,and Iwill repeat it back to you:"
prompt+="\nEnter 'quit' to end the program."
message=""
while message !='quit':
    message=input(prompt)
    print(message)
#不输入单个的quit永远不停止

#7.使用标志
#在前一个示例中，不适用于复杂情况，有的时候我们需要一个使用标志来使程序变得合理有序
active=True
while active:
    message=input(message)

    if message =='quit':
        active=False
    else:
        print(message)
#此次程序中active就是使用标志，做过于复杂的程序，找一个使用标志能够更轻松的判断程序的执行

#8.break退出循环
while active:
    message=input(message)

    if message =='quit':
        break#直接把方面那个改成break效果相当，break在任何循环中都能使用
    else:
        print(message)

#9.continue继续循环
#想要返回循环开头，不想像break那样直接跳出循环
current_number=0
while current_number<10:
    current_number+=1
    if current_number%2==0:
        continue#结束当前这一段并跳回开头
    print(current_number)

#不小心无限循环，鼠标点击运行窗口，按ctrl+c

#10.使用while循环处理列表和字典
#在列表之间移动元素
unconfirmed_users=['alice','brian','camdace']
confirmed_users=[]
#验证每个用户，直到没有未验证用户为止
while unconfirmed_users:
    current_user=unconfirmed_users.pop()

    print(f"Verrying user:{current_user.title()}")
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user)

#11.删除为特定值的所有列表元素
pets=['dog','cat','fish','cat','dog','rabbit']
print(pets)
while 'cat' in pets:#当'cat'在列表当中时就继续执行这个命令
    pets.remove('cat')#执行一次remove只能删除一个cat
print(pets)

#12.使用用户输入来填充字典
responses={}
#设置一个标志，指出调查是否继续
polling_active=True
while polling_active:
    #提示输入被调查者的名字和回答
    name=input("\nWhat is your name?")
    response=input("Which mountain would you like to clime someday?")
    #将回答存储在字典当中
    responses[name]=response#name这个键指向的值
    #看看是否还有人要参与调查
    repeat=input("would you like to let another person respond？（yes/no)")
    if repeat=='no':
        polling_active=False
print("\n---Poll Results---")
for name,response in responses.items():
    print(f"{name} would like to clime {response}")
