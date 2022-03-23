
举个例子：

```python
alien_0 = {'color': 'green','points': 5}
print(alien_0['color'])
print(alien_0['points'])
```
# 使用字典
字典：键-值对,值可以是数字string，list，tuple and even dictionary
添加键-值对应`alien_0['x_positon'] = 25`添加顺序不重要
改变值
删除就`del alien_0['points']`
多行字典,缩进四个字符，逗号,最后一行也加逗号比较好
```python
{
    'jen':'python',
    'chase':'C',
}
```
print分行用+就可以``
# 遍历字典
有多个遍历字典的方法，可遍历字典的所有键-值对、键/值
`.item()`返回一对键——值，存储到两个变量里
```python
for k,v in user_0.item()
```
字典不注重顺序，只关注键和值之间的关系、
遍历字典上的所有键`for name in user_0.keys()`遍历字典是会默认遍历所有的键`for name in user_0`也是默认访问的是键
key是返回一个列表包含所有的键
## 按顺序遍历字典中的所有键
要是要特定顺序，`sorted()`对返回的键进行排序`for name in sorted(user_0.key())`
## 遍历字典中的所有值
`values()`产生的列表可能会包含大量的重复的值，所以可以使用列表set类似list，但是每个元素都是独一无二的，`set(user_0.values())`
# 嵌套
## 字典列表
字典储存在列表中，这就是嵌套
```python
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'blue','points':15}

aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)
```
`len(aliens)`
## 字典里存储列表
`for topping in pizza['toppings']`
