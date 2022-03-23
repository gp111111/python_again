class Restaurant():
    """The opening restaurant"""


    def __init__(self,restaurant_name,cuisine_type):
        """Initialize the restaurant_name and cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        """Descirbe the restaurant and it's cuisine type"""
        print(self.restaurant_name.title() + ' is the ' +
        self.cuisine_type.title() + '.')


    def open_restaurant(self):
        """The restaurant is open"""
        print(self.restaurant_name + " is open.")
            #return '3'

#9-4
    def number(self):
        """The number of persons who """
        print(str(self.number_served) + ' persons have been eaten here.')
#方法里的第一个形参self, 其实指向的就是实例，这样也可以在每个方法里进行调用

#9-4
    def set_number_served(self,number):
        """Pass the argument of persons number"""
        self.number_served = number


    def increment_number_served(self):
        """increase the number of persons eaten in this restaurant"""
        self.number_served += 365


class IceCreamStand(Restaurant):
    """A simple try to simulate the IceCreamstand"""


    def __init__(self,restaurant_name,cuisine_type,flavors):
        """Initialize the parent class attributions"""
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors


#    def set_flavor(self,flavor):
#        """Fill the icecream flavor"""
#        self.flavor = flavor
#        self.flavors.append(self.flavor)


    def describe_flavor(self):
        """Decribe the icecream flavor"""
        for self.flavor in self.flavors:
            print("The IceCreamStand has " + self.flavor + " flavors.")


restaurant = IceCreamStand("Jade Garden","Cantonese cuisine",['strawberry',
'milk','mango','banana'])
#restaurant.set_flavor('strawberry')
#restaurant.set_flavor()
restaurant.describe_flavor()
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(22)
restaurant.increment_number_served()
restaurant.number()
#print(restaurant.open_restaurant())





'''class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()
t.prt()'''
