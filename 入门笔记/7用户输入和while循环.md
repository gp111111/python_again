# 输入变量
`input()`暂停程序，获取输入，存储到一个变量里
创建多行字符串
```python
prompt = 'If you can tell the truth'
promt += '\nYou will get libertated from the misery'
```
input输入是string，要是用数字要转换int
求模运算符%，返回余数
# While循环
让用户选择何时退出
```python
prompt = '\nTell me something, then I will repeat it back to you.'
prompt +="\nEnter 'quit' to end this program."
message = ''
while message != 'quit':
    message = input(prompt)
    print(message)
```
因为停止循环的可能有很多，使用标志，只需要检查一个条件，标志当前值是否是True，并将所有测试（是否发生将标志变成False的条件）都放在其他地方。
```python
active = True
while active:
```
## break打破循环
```python
while True:
    if message == 'quit':
        break
```
## continue
忽略余下的代码，返回到循环的开头，然后根据条件判断是否继续循环。
## 避免无限循环
需要有迭代变量iteration
ctrl+c停止无限循环
# While循环来处理列表和字典
`while users:`

```python
while 'cat' in users:
    users.remove('cat')
```
使用户填充字典
```python
#空字典
repeat = {}
#标志
active = True
while active:
    name = inpt()
    response = input()
    repeat[name] = response

```
