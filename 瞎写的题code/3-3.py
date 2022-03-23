#3-4
names = ['Cindy','Jeffery','Chris','Jean']
for i in range(4):
    print(names[i].title() + ' are invited.')
#3-5
print(names[0].title() + ' cannot attend for this dinner.')
names[0] = 'Evans'
for i in range(4):
    print(names[i].title() + ' are invited.')
names.insert(0,'Chen')
names.insert(3,'Lee')
names.append('Cai')
print(names)
for i in range(3):
    d1 = names.pop(0)
    print(d1)
del names[0:3]
print(names)
