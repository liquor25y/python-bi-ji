#1.导入整个模块
#创建一个make_pizza()的模块

import pizza#导入了一个模块，就可以调用这个模块里面的所有函数
pizza.make_pizza(16,'mushrooms')#调用make_pizza

#2.导入特定的函数
#from module_name import function0 function1 function2
from pizza import make_pizza,show_pizza
pizza.show_pizza(['mushrooms','greenpeppers'])

#3.使用as给函数指定别名
#from pizza import make_pizza as mp

#4.使用as给模块指定别名
#import pizza as p

#5.导入模块中的所有函数
from pizza import *
# *让pizza的每个函数都复制到这个程序文件中






