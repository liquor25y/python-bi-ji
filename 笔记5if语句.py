player='george'
player=='george'

#1.不相等!=
#检查多个条件 1.使用and检查条件 2.使用or检查条件
age_0=22
age_1=18
age_0>=21 and age_1>=21
age_0>=21 or age_1>=21 #为了增加可读性，加括号

age=19
if age>=18:
    print('you can come here')

#2.if-else语句
if age>20:
    print('you can vote')
else:
    print('not')

#3.使用多个elif语句
if age >20:
    print(yes)
elif age<65:
    print('not')
elif age>30:
    print('.')
#如果想要执行多个代码块，就用多个if 如果只执行一个就使用if-elis-else结构


#4.用if语句处理列表
#比萨店的青椒用完了，该如何处理
requested_toppings=['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping=='green peppers':
        print('sorry,we are out of green peppers')
    else:
        print(f"adding{requested_topping}.")
print("\nFinished making your pizza!")

#5.确定列表不是空的
requested_toppings=[]
if requested_toppings:#这一步用于检验是否是空的
    for requested_topping in requested_toppings:
        print(f"Adding{requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("are you sure you want a plain pizza?")


