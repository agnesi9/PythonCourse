#Create a class named Person that has the following attributes: name, age, and address. 
#It should also have a method called get_info() that returns a string with the person's name, age, and address.

class Person:
    def __init__(self, name:str, age:int, address:str) -> None:
        self.name = name
        self.age = age
        self.address = address

    def get_info(self):
        print("Person's name: " + self.name + ", person's age: " + str(self.age) + ", person's address: " + self.address)
    
person1 = Person("Agne", 24, "Klaipeda")
person1.get_info()