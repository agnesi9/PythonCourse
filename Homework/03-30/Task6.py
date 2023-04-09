#Create a base class named Vehicle that has the following attributes: make, model, and year. 
#It should also have a method called get_info() that returns a string with the vehicle's make, model, and year. 
#Then create two subclasses, Car and Truck, that inherit from Vehicle and add additional attributes and methods specific to each type of vehicle.

class Vehicle:
    def __init__(self, make:str, model:str, year:int) -> None:
        self.make = make
        self.model = model
        self.year = year

    def get_info(self) -> str:
        return "Vehicle's make, model and year: " + self.make + " " + self.model + " " + str(self.year)
    

class Car(Vehicle):
    def __init__(self, make: str, model: str, year: int, color:str) -> None:
        self.color = color
        super().__init__(make, model, year)

    def get_info(self) -> str:
        return super().get_info() + ", color: " + self.color

car1 = Car("Volkswagen","Golf", 2015, "black")
print(car1.get_info())
