# 列表/列表修改
列表是一系列按特定顺序排列的元素组成，变量名字是个复数比较好，元素有没有关系都可以
`name = ['Cindy','Jeffery','Chris','Jean']`
```python
names = ['Cindy','Jeffery','Chris','Jean']
print(names) #打出来的是列表全部包含括号
print(names[0])#[里面是索引，从0开始,直接是元素]
#也可以负数索引
print(names[0],title())
```
列表是动态的，创建列表需要增删元素
修改列表元素，可以修改任何元素的值
`names[0] = 'Git'`
在列表末尾中添加元素，#可以建立一个空列表，然后一个一个加元素
`names.append('element')`一个append只能加一个元素
在列表中插入元素，
`names.insert(0,'elements')`
删除元素
`del names[整数/切片slices][0:3]就是第0个到第2个数字（总共三个）`
pop()删除元素
`names.pop(0)`删除任何位置的元素，并且储存到这个变量中，删除后被弹出的元素不再列表中
移除元素
`names.remove('elements')`只能删除一个特定的值
# 组织列表
调整顺序
## 按字母排序
永久排序names.sort()
反着拍names.sort(reverse = True)
暂时排序sorted(names)
## 倒着打印列表
names.reverse()永久性改变
## 确定表的长度
len(names)计算个数就是python从1开始计算。

