#9-5&9-7
class Users:
    """login attempt number"""


    def __init__(self):
        """Initialize the arguments"""
        self.login_attempts = 0


    def increment_login_attempts(self):
        """Increase the times that users attempt to login"""
        if self.login_attempts >= 5:
            print("Trying to much")
        else:
            self.login_attempts += 1
            print('You have tried for ' + str(self.login_attempts) + '.')


    def reset_login_attempts(self):
        """Reset the login attempts times"""
        self.login_attempts = 0


class Previleges():
    """Users previleges"""


    def show_privileges(self,previleges):
        """describe the user's previlege"""
        #self.previleges = ['can add post','can delete post','can ban user']
        self.previleges = previleges
        for self.previlege in self.previleges:
            print(self.previlege)

class Admin(Users):
    """Users Inheritance"""


    def __init__(self):
        """Initialize the previleges and parent class attributions"""
        super().__init__()
        #self.previleges = ['can add post','can delete post','can ban user']
        self.previleges = Previleges()
'''这两个类里的previleges是不同的属性，尽量不要用同样的名字，容易搞混，局部变量：定义在方法中
的变量，只作用于当前实例的类。//实例变量在类的声明中，属性是用变量来表示的，这种变量就称为实例变
量。实例变量定义在方法中，使用self绑定到实例上，只是对当前实例起作用。
实例变量只能被实例对象调用'''

#times = Admin(['can add post','can delete post','can ban user'])
times = Admin()
#子类的实例调用了User类（父类的）方法
times.reset_login_attempts()
times.increment_login_attempts()
times.increment_login_attempts()
times.increment_login_attempts()
times.increment_login_attempts()
times.increment_login_attempts()
times.increment_login_attempts()
times.reset_login_attempts()
times.increment_login_attempts()
#子类实例调用了子类特殊的方法
times.previleges.show_privileges(['can add post','can delete post','can ban user'])
