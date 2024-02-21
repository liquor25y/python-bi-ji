#遍历整个列表
# 1.for循环中执行操作
magicians=['alice','david','carolina']
for magician in magicians:#在magicians中取出一个名字与变量magician相关联
    print(magician)


for magician in magicians:
    print(magician.title(),"was a trick")
for magician in magicians:
    print(f"{magician.title()}, was a trick")

#2.for循环结束后执行一些操作（没有缩进，不参与for循环的执行）
#3.for循环必须接冒号，告诉计算机下一行是循环的第一行


#4.产生一系列数range()
for value in range(1,5):#含首不含尾
    print(value)

#5.将数字变为数字列表list()
numbers=list(range(1,5))
for number in numbers:
    print(number)

#6.range指定步长
for number in range(2,11,2):#第三个参数为指定步长
    print(number)

#7.对数字列表执行简单的统计计算
digits=[1,2,3,4,5,6,7,8,9,0]
print(min(digits))
max(digits)
sum(digits)
sum(digits)/len(digits)

#8.列表分析列表分析将for循环和创新信元素的代码合并成一行（简化列表）
squares=[value**2 for value in range(1,5)]
print(squares)
#用这种语法，要先指定一个描述性的列表名，然后指定一个左方括号并定义一个表达式，用于生成要储存在列表中的值

#squares：指定的一个描述性的列表名
#value**2：表达式
#for 循环，为表达式提供值 加上右方括号

#9.使用列表的一部分
#切片
players=['george','westbrook','leonard','harden']
print(players[0:1])#含首不含尾
#若没有指定第一个索引，直接从头开始,没有指定第二个同理
print(players[:2])
print(players[2:])
#寻找最后三个成员
print(players[-3:])

#10.遍历切片
for player in players[:2]:
    print(player.title())

#11.复制切片 players1=players2[:]
players=['george','westbrook','leonard','harden']
players1=players[:]
for player in players1[:2]:
    print(player.title())

#如果不使用切片直接复制 players=players1
players=['george','westbrook','leonard','harden']
players1=players
players.append('curry')
players1.append('sga')
print(players)
print(players1)
#两者在进行添加过后，不能在不同列表增加各自的球星，换句话说，两个表不是分开的

