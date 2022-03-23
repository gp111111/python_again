#测试修改属性，不能回调odometer，属性修改是针对同一个实例来说的
class Car():

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def read_odometer(self):
        print("The car's odometer is " + str(self.odometer_reading) + ".")


    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer.")


    def increase(self,miles):
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("Please check the miles")


my_new_car = Car('audi','a4','2016')
my_new_car.read_odometer()
my_new_car.update_odometer(45)
my_new_car.read_odometer()
my_new_car.increase(-23)
my_new_car.read_odometer()

his_new_car = Car('audi','a4','2016')
his_new_car.update_odometer(23)
his_new_car.read_odometer()
