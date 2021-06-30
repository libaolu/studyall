"""
#使用def定义函数

#定义add()函数
def add(a,b):
    print(a+b)

#调用add()
add(1,2)

#通常add函数不会直接打印，将结果通过return关键字返回，使用变量c接收add函数返回的值，并使用print()方法打印
def add(a,b):
    return a+b

haole= add(1,3)
print(haole)
"""


#调用的时候不传参，add函数使用默认参数计算，否则使用参数的值
def add(a=1,b=3):
    return a+b

c1 = add()
c2 = add(2,10)
print(c1)
print(c2)