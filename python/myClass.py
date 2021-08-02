# coding=UTF-8

#类和方法

#定义class类

class myClass(object):
    def say_hello(self,name):
        return "hello," + name


#调用class类
mc = myClass()
print(mc.say_hello("lbb"))


#object为所有类地基类，所有类在创建时默认继承object（不声明继承object也可以）
#方法创建时同样使用def方法，与函数地唯一区别是方法地第一个参数必须声明，习惯命名为self，在调用这个方法时不需要为该参数设置数值