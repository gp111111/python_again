filename = 'guest.txt'

i = 0
active = 'a'
with open(filename,'a') as file_object:

    while active:
        name = input("Please enter your name: ")
        file_object.write(name + '\n')
        i += 1
        if i > 3:
            print('The persons here are enough.')
            break




def count_words(filename):
    """Calculate the words included in the file"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = "sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + "has about " + str(numwords) + " words.")

filenames = ['alice.txt','idea.txt','sd']
for filename in filenames:
    count_words(filename)
#运行结果可以看书99页
