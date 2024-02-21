#1.在文件中读取数据
#创建一个保留圆周率后30为小数的值
with open('pi_digits.txt') as file_object:#open()打开文件
    contents=file_object.read()#读取文件中的全部内容 最后内容多出一个空行（read的特性）
print(contents)
print(contents.rstrip())#倘若不想要那个空行，使用rstrip()

#2.文件路径
#当寻找pi_digits的文件时，寻找当前文件目录中的文件，若不在则无法调用
#如果不存在当前文件目录 但在当前文件目录中的文件夹中 则可以
with open('text_files/filename.txt') as file_object:#（相对路径）
    data=file_object.read()
print(data)
print(data.rstrip())
    #这行代码让python寻找当前文件中的文件夹内的文件

#3.绝对路径
#所需文本不在当前文件夹中，则使用绝对路径
file_path='E:\\PycharmProjects\\pythonProject5\\pi_digits.txt'#要用双斜杠
file_path='E:/PycharmProjects/pythonProject5/pi_digits.txt'#这样也可以
with open(file_path) as file_object:
    pi=file_object.read()
print(pi)

#4.逐行读取
filename='pi_digits.txt'#利用for循环即可逐条读取 无关命名

with open(filename) as file_object:
    for line in file_object:
        print(line)
        #print(line.rstrip())和先前的直接读取效果相同

#5.创建一个包含文件各行内容的列表
with open(filename) as file_object:
    lines=file_object.readlines()#读取一行 存储在一个列表中 将列表赋值给lines
for line in lines:
    print(line.rstrip())#同上
    #使用文件的内容
pi_string=''
pi_string1=''
for line in lines:
    pi_string +=line.rstrip()
    pi_string1+=line.strip()#用strip可以删除每行左边的空格
print(pi_string)
print(pi_string1)
print(len(pi_string))
print(len(pi_string1))

#6.包含一百万位的的圆周率
filename='pi_hundred_digits.txt'#一百万为找不到拿一百位代替
with open(filename) as file_object:
    lines=file_object.readlines()
pi_hundred_string=''
for line in lines:
    pi_hundred_string+=line.strip()
print(f"{pi_hundred_string[:52]}...")#只打印到小数点后五十位
print(len(pi_hundred_string))

#7.#圆周率内包含你的生日吗
for line in lines:
    pi_string+=line.strip()

birthday=input("Enter your birthday,in the form mmddyy:")
if birthday in pi_string:
    print("your birthday appears in the first million digits of pi!")
else:
    print("your birthday does not appear in the first million digits of pi.")

#8.写入文件write
#注意：如果写入的文件不存在，自动创建 如果写入的文件已经存在 将自动清空原有文件！
filename='programming.txt'
with open(filename,'w')as file_object:
    file_object.write("I love programming.")
    file_object.write("I love it.")#写入多行
with open(filename)as file_object:
    data=file_object.read()
print(data)

#9.附加到文件
#若需要加到文件原本的内容中而不是覆盖原有内容 需要使用附加模式："a"
with open(filename,'a')as file_object:
    file_object.write("I also like sweet")