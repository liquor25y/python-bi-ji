#1.定义函数
def greet_user():
    print("hello!")
greet_user()

#2.向函数传递信息
def greet_user(username):
    print(f"Hello,{username.title()}!")

greet_user('jeese')

#传递实参
#3.位置实参 函数关联方式最简单的是实参的顺序，这也被成为位置实参
def describe_pet(animal_type,pet_name):#形参
    print(f"\nI have a {animal_type}")
    print(f"It's name is {pet_name}")

describe_pet('dog','张航')#按照位置顺序赋值给形参

#4.关键字实参
def describe_pet(animal_type,pet_name):#形参
    print(f"\nI have a {animal_type}")
    print(f"It's name is {pet_name}")
describe_pet(animal_type='dog',pet_name='张航')
describe_pet(pet_name='张航',animal_type='dog')

#5.默认值
#发现大部分人的宠物类型都是小狗时，直接在定义还函数的时候将animal_type设为dog
def describe_pet(pet_name,animal_type='dog'):#这个默认值一定要放在最后，如果不放在最后，运行不了（不知道原因）
    print(f"\nI have a {animal_type}")
    print(f"It's name is {pet_name.title()}")
describe_pet(pet_name='张航')
#如果宠物的类型不是狗狗
describe_pet(pet_name='杨威',animal_type='monkey')

#6.等效的函数调用
#对于上述函数
#一条名为Willie的小狗
describe_pet('willie')
describe_pet(pet_name='willie')
#一只名为Harry的仓鼠
describe_pet('hatty','hamster')
describe_pet(pet_name='hatty',animal_type='hamster')
describe_pet(animal_type='hamster',pet_name='hatty')

#避免实参错误
def describe_pet(animal_type,pet_name):
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

#7.返回值
def get_formatted_name(first_name,last_name):
    full_name=f"{first_name}{last_name}"
    return full_name.title()
musician=get_formatted_name('luka','donic')
#调用返回值的函数时，需要提供一个变量以便于将值赋给它
print(musician)

#8让实参变成可以选择的
#有的人有中间名，有的人没有，这种情况如何解决
def get_formatted_name(first_name,middle_name,last_name):
    full_name=f"{first_name} {middle_name} {last_name}"
    return full_name.title()
musician=get_formatted_name('john','lee','hooker')
print(musician)

#为了使情况适用于有的人没有中间名
def get_formatted_name(first_name,last_name,middle_name=''):#和其他不一样的地方
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name}  {last_name}"
    return full_name.title()

musician=get_formatted_name('jimi','hendrix')
print(musician)
musician=get_formatted_name('john','hooker','lee')
print(musician)

#9.返回字典
def build_person(first_name,last_name):
    person={'first':first_name,'last':last_name}
    return  person
musician=build_person('jimi','hendrix')
print(musician)#将两个值存入字典当中

#10.适当修改函数结构 使函数存储年龄
def build_person(first_name,last_name,age=None):#None可视为占位值
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age']=age
    return  person
musician=build_person('jimi','hendrix',age=27)
print(musician)

#11.通过使用while一直执行函数
def get_formatted_name(first_name,last_name):
    full_name=f"{first_name} {last_name}"
    return full_name.title()
while True:#这是一个无限循环
    print("\n please tell me your name:")
    f_name=input("First name:")

    if f_name=='q':
        print("quit it successfully")
        break

    l_name=input("Last name:")
    if l_name=='q':
        print("quit it successfully")
        break

    formatted_name=get_formatted_name(f_name,l_name)
    print(f"\nHello,{formatted_name}")

#12.传递列表
def greet_users(names):
    for name in names:
        msg=f"Hello {name.title()}"
        print(msg)
names=['george','doncic','westbrook','curry']
greet_users(names)

#13.在函数修改列表
#需要打印的设计存储在一个列表打印后转移到另一个列表
unprinted_designs=['phone case','robot pendat','dodecahedron']
completed_models=[]
#模拟打印每个设计，直到没有未打印设计为止
while unprinted_designs:
    current_design=unprinted_designs.pop()
    print(f"Printing model:{current_design}")
    completed_models.append(current_design)
print("\nThe following models have been printed")
for model in completed_models:
    print(model)

#14.将上述代码制作成函数
def print_models(unprinted_models,completed_models):
    while(unprinted_models):
        unprinted_model=unprinted_models.pop()
        print(f"Printing model {unprinted_model}")
        completed_models.append(unprinted_model)
def show_completed_models(completed_models):
    print("The following models have been printed")
    for completed_model in completed_models:
        print(completed_model)
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

#15.禁止函数修改列表
#使用列表切片制作副本
print_models(unprinted_designs[:],completed_models)
print(unprinted_designs)

#16.传递任意数量的实参
#有的时候预先不知道要接受多少个实参，python可以在函数中确定语句所需的实参
def make_pizza(*toppings):#没有实参，只有形参toppings
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers')

#17.结合使用位置实参和任意数量实参
def make_pizza(size,*toppings):#没有实参，只有形参toppings

    print(f"\nMaking a {size}-inch pizza with following toppings:")
    for topping in toppings:
        print(toppings)
make_pizza(6,'pepperoni')
make_pizza(12,'mushrooms','green peppers')

#18.使用任意数量的关键字实参
def build_profile(first,last,**user_info):#**表示让python创建一个空字典 名为user_info
    #创建一个字典，其中包括我们知道的有关用户的一切
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info
user_profile=build_profile('albert','einstein',location='princeton',field=
                           'phyics')
print(user_profile)




