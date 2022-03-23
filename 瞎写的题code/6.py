#6-1
person_1 = {
    'first_name': 'Andrew',
    'last_name': 'Chris',
    'city': 'Newyork',
    }
print(person_1['first_name'])
print(person_1['last_name'].title())
print(person_1['city'].title())
#6-4
for information in person_1.keys():
    print(information)
for content in person_1.values():
    print(content)
#6-5
river = {}
river['Huanghe'] = 'China'
river['Mississippi River'] = 'USA'
river['nile'] = 'egypt'
print(river)
for keys,values in river.items():
    print('The {} runs through {}.'.format(keys.title(),values.title()))
if 'England' not in river.values():
    print("Please take the inverstigate.")
