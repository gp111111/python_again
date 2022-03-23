#存储数据
import json

def get_stored_user():
    """如果已经存储用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username =json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
    return username


def greet_user():
    """问候用户，并指出其名字"""
    username_login = input("Please enter your name: ")
    username = get_stored_user()
    if username:
        if username_login == username:
            print("Welcome back, " + username + " !")
        else:
            print("Please check your name.")
            
    else:
        print("Ok, you are new here.")
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")
greet_user()
