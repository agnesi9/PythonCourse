#Create a class named Car that has the following attributes: make, model, and year. 
#It should also have a method called get_info() that returns a string with the car's make, model, and year

class Car:
    def __init__(self, make:str, model:str, year:int) -> None:
        self.make = make
        self.model = model
        self.year = year

    def get_info(self) -> str:
        print("Car's make, model and year: " + self.make + " " + self.model + " " + str(self.year))
    
car1 = Car("volkswagen","golf",2015)
Car.get_info(car1)
car1.get_info()