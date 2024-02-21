#列表定义：一系列按特定顺序排列的元素组成
#在python中用（[]）表示
players=['george','harden','leonard']
print(players)

#1.访问列表元素 索引从0开始 访问的元素不包括方括号
print(players[0])
print(players[0].title())
print(players[0].upper())

#2.索引是负数从后面开始
print(players[-1].title())
#用f将列表信息提取 引用列表元素用中括号
message=f"My fasvorite basketball player is {players[0].title()}"
print(message)

#3.修改列表元素
print(players)
players[2]='curry'
print(players)

#4.添加元素
#在列表末尾添加元素append
players.append('curry')
print(players)
#在列表中插入元素
players.insert(1,'Westbrook')
print(players)#在原先的索引位置上插入，其他的向右边排


#5.用del语句删除元素
del players[2]
print(players)
#用pop()语句删除元素 （有的时候删除了列表数据还需要数据，如外星人在x,y坐标死了，得保留死亡位置）
#pop()与语句类似于将元素弹出列表，优先弹出最后的那个元素
print(players)
poped_players=players.pop()
print(players)
print(poped_players)

#弹出任意位置元素
print(players)
favorite=players.pop(0)
print(players)
print(f"My favorite player is {favorite.title()}")

#根据值删除元素remove()
players=['george','harden','leonard']
print(players)
players.remove('harden')
print(players)

#用remove的同时保留剔除元素的值
#提前赋值
favorite='george'
players.remove(favorite)
print(f"My favorite palyers is {favorite.title()}")


#6.使用sort()对列表永久排序 按照首字母排序
players=['george','harden','leonard']
players.sort()
print(players)

#按照字母顺序相反的顺序排列元素(resverse=True)
players.sort(reverse=True)
print(players)

#临时排序sorted()
#可以用于需要排序的时候，但不改变本身的顺序
print(players.sorted())#这句话不可用
print((sorted(players)).reverse())#????怎么用sorted按字母顺序相反的方式打印

#7.倒着打印列表reverse() 永久反转
print(players)
players.reverse()
print(players)

#8.确定列表的长度
len(players)





