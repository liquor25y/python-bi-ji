#刚开始有点看不懂概念 看完回来补
#1.创建Dog类
class Dog:
    "一次模拟小狗的简单尝试"
    def __init__(self,name,age):#初始化方法：该方法命名两边必须有两条下划线！！！！

#三个形参，其中self必不可少 代表示例dog本身 每个与实例相关
#的属性都将上传给self self不需要赋值 只需要给其他形参（name和age）提供值
        "初始化属性name和age"
        self.name=name
        self.age=age
    def sit(self):
        "模拟小狗收到命令时蹲下"
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        "模拟小狗收到命令时打滚"
        print(f"{self.name} rolled over!")
#创建Dog类之后，我们赋予了每条小狗蹲下sit 和打滚rolled_over的能力
#方法_init_()
#类中的函数称为方法 （在编写方法时加两条横线，这样方便与普通函数区分）

#2.根据类创建实例

my_dog=Dog('Willie',6)
print(f"My dog's name is {my_dog.name}")
print(f"My dog's age is {my_dog.age}")

#访问属性
my_dog.name
#调用方法
my_dog.sit()
my_dog.roll_over()

#3.创建多个实例
my_dog=Dog('willie',6)
your_dog=Dog('lucy',3)

print(f"My dog's name is {my_dog.name}")
print(f"My dog's age is {my_dog.age}")
my_dog.sit()

print(f"\nMy dog's name is {your_dog.name}")
print(f"My dog's age is {your_dog.age}")
your_dog.sit()

#4.实用类和实例
#编写一个表示汽车的类
class Car:
    "一次模拟汽车的简单尝试"
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0#默认值

    def increment_odometer(self,miles):
        "将里程表读书增加指定的量"
        if miles >=0:
            self.odometer_reading+=miles
        else:
            print("禁止回调数据")
    def get_descriptive_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def update_odometer(self,mileage):#通过方法修改值
        "将里程表读数设置为指定的值"
        self.odometer_reading=mileage

    def read_odometer(self):#读取默认值
        print(f"This car has {self.odometer_reading} miles on it")

my_new_car= Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading=23#直接修改属性的值
my_new_car.update_odometer(24)
my_new_car.read_odometer()

#5.给属性指定默认值
#有些属性无需通过形参来定义 可以在init中指定默认值
#新车子默认里程为0（看上面的代码，新添默认值）

#6.修改属性的值
#方法一：直接修改属性的值（看上面）
#方法二：通过方法修改属性的值（也看上面）

#7.通过方法对属性的值进行递增（看上面）
my_used_car=Car('subaru','outback',2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)#可以通过修改方法代码，禁止回调里程
my_used_car.read_odometer()

#8.继承：当要编写的类是另一个现成类的特殊版本，可以使用继承 新的类是子类 被继承的是超（父）类
#子类的方法 __init__
#创建一个新的特殊版本的类
class ElectricCar(Car):#创建子类时，超类必须包含在当前文件当中
    def __init__(self,make,model,year):
        #初始化父类的属性
        super().__init__(make,model,year)#super()，能够帮助调用超类
        #在初始化电动车特有的属性
        self.battery=Battery()#调用下面的类

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")
        #如果有人想对电动车调用油箱，忽略car中的直接用电车的
    def describe_battery(self):#给子类定义属性和方法
        #打印一条关于电池容量的消息
        print(f"This car has a {self.battery_size}-kwh battery.")


my_tesla=ElectricCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

#9.给子类定义属性和方法 看上面

#10.重写父类的方法 看上面
#原本的车子也许有油箱，但是电车没有，油箱属性对于新类来说没什么用
#重写可以继承精华，去除糟粕


#11.将实例作为属性
#我们可以创建一个battery的类 将battery作为electricar的属性
class Battery:
    '一次模拟电动汽车电瓶的简单尝试'
    def __init__(self,battery_size=75):
        "初始化电瓶的属性"
        self.battery_size=battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery.")

class ElectricCar(Car):#创建子类时，超类必须包含在当前文件当中
    def __init__(self,make,model,year):
        #初始化父类的属性
        super().__init__(make,model,year)#super()，能够帮助调用超类
        #在初始化电动车特有的属性
        self.battery=Battery()#调用下面的类
my_tesla=ElectricCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()#连续的调用类

#12.导入类
#随着不断给类添加功能，需要妥善的使用继承

from car import Car
#从文件car中引入Car的类
my_new_car=Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading=23
my_new_car.read_odometer()

#13.在一个模块中存储多个类 导入多个类
from car import ElectricCar,Car

my_beetle=Car('volkswagen','beetle',2019)
print(my_beetle.get_descriptive_name())

my_tesla=ElectricCar('Tesla','roadster',2019)
print(my_tesla.get_descriptive_name())

#导入模块
import car
#导入模块所有类
from car import *

#14.使用别名
from car import ElectricCar as EC
my_tesla=EC('tesla','roadster',2019)





