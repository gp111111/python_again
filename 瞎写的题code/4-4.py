#切片，复制列表，并且循环
numbers = [value**3 for value in range(1,11)]
values = numbers[:]
numbers.append(300)
values.append(400)
print('numbers include: ')
for number in numbers:
  print(number)
print('values include: ')
for value1 in values:
  print(value1)
#元组tuple
foods = ('fried chicken','piiza','milk tea','fish','hot pot')
for food in foods:
  print(food)
foods = ('taco','piiza','milk tea','fish','eggs')
for food in foods:
  print('modified_foods:{}'.format(food))
 #代码格式不超过80个字符
 #易于阅读
 #PEP8缩进使用四个空格
