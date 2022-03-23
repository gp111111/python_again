#5-3,5-4，5-5
alien_color = input("Please choose the alien_color \
among green,yellow, and red: ")
print(alien_color)
print(id(alien_color))
#注意is和==的区别is比较的是id是否是一样的，==比较的是值是否是一样的
if alien_color == 'green':
    print("The player scored five points.")
    print(id('green'))
elif alien_color == 'yellow':
    print("The player scored ten points.")
elif alien_color == 'red':
    print("The player scored fifteen points.")

#5-6
age = 15
if age<2:
    print('He is an infant.')
elif age<4:
    print('He is in the age of learning how to walk.')
elif age<13:
    print('He is a child.')
elif age<20:
    print('He is a teenager.')
elif age<65:
    print('He is an adult.')
elif age>=65:
    print('He is a senior citizen.')
#5-8,5-9,
users_names = ['admin','Sam','Tim','Jess','Grace']
if users_names:
    for user in users_names:
        if user == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello ' + user + ', thank you for logging in again.')
else:
    print('We need to find some users')
#5-10
users_names = ['admin','Sam','Tim','Jess','Grace']
current_names = users_names[:]
new_names = users_names[0:2]
new_names.append('Judy')
new_names.insert(0,'Cindy')
new_names.append('Monica')
current_names1 = []
for current_name in current_names:
    current_names1.append(current_name.upper())
print(current_names1)
for new_name in new_names:
    new_name = new_name.upper()
    if new_name in current_names1:
        print(new_name)
        print("This user name has been utilized, choose another user name \
please.")
    else:
        print(new_name)
        print('This user name has not been utilized')
