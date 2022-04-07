from random import randint

class Die():
    """present a die class"""

    def __init__(self,num_sides=6):
        """the number of die initial faces is 6"""
        self.num_sides = num_sides

    def roll(self):
        """return an int between 1 and the number of die faces"""
        return randint(1,self.num_sides)