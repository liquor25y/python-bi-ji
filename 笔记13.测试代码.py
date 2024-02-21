#测试代码 unittest
#先创建一个继承unittest.TestCase的类 并编写一系列方法对函数行为的不同方面进行测试
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):#创建了一个针对该函数进行测试的类
    def test_first_last_name(self):
        formatted_name=get_formatted_name('janis','joplin')
        self.assertEquals(formatted_name,'Janis Joplin')
        #将formatted_name与后面那个'Janis Joplin' 做比较 如果一样就完事大吉 如果不一样就说一声

if __name__=='__main__':
    unittest.main()


