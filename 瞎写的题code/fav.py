#10-11
import json


filename = 'fav_num.json'
try:
    with open(filename) as f_obj:
        fav_num = json.load(f_obj)
except FileNotFoundError:
    with open(filename,'w') as f_obj:
        fav_num = input("Please tell me your favorite number: ")
        json.dump(fav_num,f_obj)
        print("Ok. I will remember that.")
else:
    print("I know your favorite number! It's " + fav_num + ".")
