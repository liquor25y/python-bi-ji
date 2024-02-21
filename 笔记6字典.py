#1.下面是一个简单的字典
alien_0={'color':'green','points':'5'}
print(alien_0['color'])
print(alien_0['points'])

#字典是一系列键值对，每个键都与一个值相关联，你可以用键来访问相关联的值
alien_0={'color':'green','points':'5'}
#键值对是两个相关联的值，指定键时，python会返回相关联的值，用键值之间用冒号间隔，键值对之间用逗号
#一个字典中几个键值对都可以

#2.访问字典中的值
alien_0={'color':'green','points':'5'}
new_points=alien_0['points']
print(f'you just earned {new_points}points!')

#3.添加键值对
#字典是一种动态结构，可随时在其中添加键值对，
alien_0={'color':'green','points':'5'}
print(alien_0)
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

#4.先创建一个空字典
alien_0={}#然后可以再慢慢加

#5.修改字典中的值
alien_0={'color':'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color']='yellow'
print((f"The alien now is {alien_0['color']}"))

#6.删除键值对del
alien_0={'color':'green','points':'5'}
print(alien_0)

del alien_0['points']
print(alien_0)

alien_0['points']=5
print(alien_0)

#7.由类似对象组成的字典
#字典也可以用于储存众多对象的同一种信息
favorite_languages={'jen':'python','siri':'c','yb':'mat'}
language=favorite_languages['siri']
print(f"siri's favorite language is {language}.")

#8.使用get()来访问值
#如果指定的键不存在就会出错
alien_0={'color':'green','speed':'slow'}
print(alien_0['points'])#将出现错误

#使用get()时再指定的键不存在时可返回一个默认的值
point_value=alien_0.get('points','No point value assigned.')
print(point_value)#get()第一个参数用于指定键，第二个参数为指定指定的键不存在时要返回的值，可有可没有
point_value=alien_0.get('points')#返回的默认的值为none
print(point_value)

#9.遍历字典items()

user_0={'username':'efermi','first':'enrico','last':'fermi'}
for key,value in user_0.items():
    print(f"\nkey:{key}")
    print(f"value:{value}")
#声明两个变量，用于存储键值对中的键和值value和key
#方法items(),返回一个键值对列表 ，并将键值赋给key 和value


#10.遍历字典所有的键keys()
user_0={'username':'efermi','first':'enrico','last':'fermi'}
for item in user_0.keys():
    print(item.title())
#遍历字典时会默认遍历字典中的键
for item in user_0:#与上述等价
    print(item)

#11.只给朋友发消息
favorite_languages={'jen':'python',"sarah":'c','edward':'ruby','phil':'python'}
friends=['phil','sarah']
for name in favorite_languages.keys():
    print(f'Hi {name.title()}')
    if name in friends:
        language=favorite_languages[name].title()
        print(f"\t{name.title()},I see you love {language}")
#12.确定某人没有接受调查
if 'erin' not in favorite_languages.keys():
    print("erin,you are not in here")

#13.按照特定顺序遍历字典中的所有键
favorite_languages={'jen':'python',"sarah":'c','edward':'ruby','phil':'python'}
for name,language in sorted(favorite_languages.items()):
    print(f'{name.title()},thank you for taking the poll,your favorite language is {language.title()}')

#14.遍历字典的所有值values()
for language in favorite_languages.values():
    print(language)
#上述打印出的language会出现重复
#15.剔除重复项set()
for language in set(favorite_languages.values()):
    print(language)

#16.字典和集合的区别，都是花括号，集合里面只有单个值（没有冒号），字典有键值对
{'george','leonard','westbrook'}

#17.嵌套
#字典列表
alien_0 = {'color': 'green', 'points': '5'}
alien_1 = {'color': 'yellow', 'points': '10'}
alien_2 = {'color': 'red', 'points': '15'}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

#18.创造30个外星人
#先创建一个用于存储外星人的空列表
new_aliens=[]
alien_0 = {'color': 'green', 'points': '5'}
for alien_number in range (30):
    new_alien=alien_0
    new_aliens.append(new_alien)
for alien in new_aliens[:5]:
    print(alien)

#显示创建了多少个外星人
print(f"The total number of aliens is {len(new_aliens)}")

#19.在字典中存储列表
pizza={'crust':'thick','toppings':['mushrooms','extra cheese']}
#概述所点的披萨
print(f"You ordered a {pizza['crust']}-crust pizza"#调用字典中的元素
      "with the following toppings")
for topping in pizza['toppings']:
    print("\t"+topping)

#20.在字典中储存字典
users={
    'aeinstein':{'first':'albert','last':'einstein','location':'princetion'
    },
    'mucrie':{'first':'marie','last':'curie','location':'paris'}
}
for user_name,user_info in users.items():
    print(f"\nUsername:{user_name}")
    full_name=f"{user_info['first']}{user_info['last']}"
    location=user_info['location']

    print(f"\tFull name:{full_name.title()}")
    print(f"\tLocation:{location.title()}")