#8-12
def sandwich(*ingredients):
    """对配料进行复述"""
    for ingredient in ingredients:
        print("-" + ingredient)

sandwich('ham')
sandwich('tomato','broccoli','bread')


#8-13
def profile(first,last,**user_info):
    """制作个人档案"""
    profile ={}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile
#下面这两种输出不一样上面会把user——info当键的值,关键字实参就是 ‘=’
'''a = profile(last = 'Pu',first = 'Guo',user_info ={'location':'Shanghai',
'expertise': 'electronics'} )'''

a = profile(location = 'Shanghai',expertise = 'electronics',
last = 'Pu',first = 'Guo')

print(a)
