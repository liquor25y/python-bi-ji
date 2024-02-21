##1.修改字符串的大小写

##（1）title()改变将首字母变成大写
name="ada lovelace"
print(name.title())
##name后面的句点(.)--让python对变量name执行方法title()指定

##title后面的圆括号--方法需要提供额外的信息来完成工作，但title没有额外信息，所以为空括号
##(2)全部大写/小写
print(name.upper())
print(name.lower())


##2.在字符串中使用变量

##例子：你可能想使用两个变量分别表示名和姓，然后合并两个值以显示姓名
first_name="ada"
last_name="lovelace"
full_name=f"{first_name} {last_name}"
print(full_name)
##f字符串，f是format（设置格式）的简写，因为python通过吧花括号内的变量替换为其值来设置字符串的格式

#更多应用
print(f"Hello,{full_name.title()}!")
#还可以用f字符串来创建消息
message=f"Hello,{full_name.title()}!"
print(message)

##3.使用制表符或换行符来增加空白
print("python")
print("\tpython")##缩进
print("Languages:\nPython\nC\nJavaScript")

##4.删除空白rstrip()只能够去除字符串末尾的空白，不能去除字符串和字符串之间的空白
##lstrip()去除字符串末尾的空白 strip()去除两端
favorite_language='python a '
favorite_language
favorite_language.rstrip()
favorite_language.strip()



