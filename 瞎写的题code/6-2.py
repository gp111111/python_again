#6-7
people = {
    'GuoPu': {
        'first_name':'Pu',
        'last_name':'Guo',
        'city':'Shanghai',
        },
    'GuoYaxue': {
        'first_name':'Yaxue',
        'last_name':'Guo',
        'city':'North Carolina',
        },
    'JiaZhongxun':{
        'first_name':'Zhongxun',
        'last_name':'Jia',
        'city':'Beijing',
        },
    }
for name,information in people.items():
    print(type(name))
    print('\n' + name +':')
    print('\tEnglish_version of full name:' + information['first_name'].title() +
     ' ' + information['last_name'])
    print('\tHe/She lives in ' + information['city'])


people = {
    'GuoPu': ['Shanghai','Beijing','Nanyang'],
    'GuoYaxue': ['Newyork','Shanghai','Washington'],
    'JiaZhongxun':['Beijing','Nanyang'],
    }
for name, cities in people.items():
    #print('\n')
    print(type(name))
    print(type(cities))
    print(name + ' likes the cities:')
    for city in cities:
        print('\t' + city)
