number=input("How many people do you have?")
if int(number) >8:
    print("Sorry, there is not free table for 8 people")
else:
    print("Welcome!")

number=input("please input an number")
if int(number)%10==0:
    print('是十的整倍数')
else:
    print('it is not')

def make_car(builder,type,**car_info):
    car_info['Manufacturers']=builder
    car_info['type']=type
    return car_info
car=make_car('subaru','outback',color='blue',tow_package=True)
print(car)

class restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.name=restaurant_name
        self.type=cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant's name is {self.name}")
        print(f"The restaurant's cuisine type is {self.type}")

    def open_restaurant(self):
        print("The restaurant is opening at the moment")

nanyang=restaurant('nanyang','zaocha')
bingsheng=restaurant('bingsheng','cantonese cuisine')
yuanshengju=restaurant('yuanshengju','dongbei cuisine')

nanyang.describe_restaurant()
bingsheng.describe_restaurant()
yuanshengju.describe_restaurant()

bingsheng.open_restaurant(nanyang)

print(5/0)