#input()
persons_number = int(persons_number)
if persons_number > 8:
    print('Sorry, there is no free table left.')
else:
    print('Follow me.')


#while loop
#定义这个message，就是让程序有一个可检查的量，像for，是后面返回的值存储到for后的变量名字里
prompt = '\nTell me something, then I will repeat it back to you.'
prompt +="\nEnter 'quit' to end this program."
message = ''
while message != 'quit':
    message = input(prompt)
    print(message)


#7-4
toppings =[]
prom = '\nPlease enter the topping that you would like.'
prom += "\nIf you would to stop,please enter the 'quit'."
active = True
while active:
    topping = input(prom)
    if topping == 'quit':
        active = False
        continue
    print('\nWe would add {} into the pizza that +
    you ordered.'.format(topping))

#7-5
prom = "\nPlease tell us what age are you: "
i = 0
while True:
    age = int(input(prom))
    i += 1
    if age < 3:
        print('The ticket fee is $3.')
    elif age <= 12:
        print('The ticket fee is $10.')
    elif age > 12:
        print('The ticket fee is $15.')

    if i > 4:
        print('Sorry,there are more than {} people.'.format(i))
        break


#7-8,7-9

sandwich_orderes = [
    'Familymat',
    'Pastrami'
    'Lawson',
    'Pastrami',
    'Macdownald',
    'Pastrami',
    ]
finished_sandwiches = []
while 'Pastrami' in sandwich_orderes:
    sandwich_orderes.remove('Pastrami')
    #finished_sandwiches.append(finished_sandwiche)
print(sandwich_orderes)

#7-10
locations ={}
active = True
while active:
    name = input("\nWhat's your name? ")
    location = input("If you could visit one place in the world, where would \
you go?")
    locations[name] = location
    flow = input("Is there more people who would like to take the survey: \
yes/no?")
    print(locations)
    if flow =='no':
        active = False
        #break
