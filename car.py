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
