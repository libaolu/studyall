#字典用花括号表示
#python中规定一个字典中key必须是唯一的，value可以相同

#定义字典
dicts = {"username":"li","age":"18"}

#打印字典里所有的key
#keys()方法返回字典key的列表
print(dicts.keys())

#打印字典里所有的value
#values()方法返回字典value的列表
print(dicts.values())


#循环打印字典里的key.value
#items方法将所有的字典以列表形式返回
for k,v in dicts.items():
    print("keys is %r" %k)
    print("values is %r" %v)

#删除键是age的项
#pop方法通过指定key来删除字典中的某元素
dicts.pop("age")

#打印字典以列表的方法返回
print(dicts.items())