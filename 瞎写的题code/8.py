#8-3
def make_shirt(size,character):
    """customize shirts with following information"""
    print("The shirt size is " + size + ".")
    print("And the character is " + character + ".")

size = input('\nplease inform us what size would you like: ')
character = input('please inform us what character would you like: ')
make_shirt(size, character)
#验证发现这个形参函数定义的应该不是变量名字，所以可以互换赋值def里size不是变量size
#为了防止搞混还是不要这样做吧,形参和实参不要是同样的名字

#8-6
def city_country(city,country):
    """确定城市所在国家"""
    c_c = city.title() + ','+ country.title()
    return c_c

solution = city_country("Santiago","Chile")
print(solution)


#8-7 8-8制作唱片文档
def make_album(name,singer,songs_number=''):
    """制作唱片字典"""
#input是在外部

    album_dictionary = {'name':name,'singer':singer}
    if songs_number:
        album_dictionary['songs_number'] = songs_number
    return album_dictionary
albums =[]
while True:
    name = input("album name: ").title()
    singer = input("singer name: ").title()
    songs_number = input("if you know songs number,please enter: if you don't \
know,please enter 'No'.")
    if songs_number == "No":
        songs_number =''
    a_d = make_album(name,singer,songs_number)
    albums.append(a_d)
    print(albums)


#8-9
def show_magicians(magicians):
    """输出每个users名字"""
    for magician in magicians:
        print(magician)

def make_great(magicians,magicians1):
    """在名字前加修饰词"""
    #magicians1 =[]
    while magicians:
        magician = "the Great " + magicians.pop()
        print(magicians)
        magicians1.append(magician)
    return magicians

users = ['a','b','c']
users1 =[]
make_great(users[:],users1)
print(users)
show_magicians(users1)
