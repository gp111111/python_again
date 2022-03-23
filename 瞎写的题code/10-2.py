#10-6
print("Give me two numbers, and I'll sum them.")
print("Enter 'q' to quit")


while True:
    number1 = input("First number: ")
    if number1 == 'q':
        break
    number2 = input("Second number: ")
    if number2 == 'q':
        break


    try:
        sum_num = int(number1) + int(number2)
    except ValueError:
        msg = "Please enter the number instead of text."
        print(msg)
    else:
        print(sum_num)
