#Create a base class named Person that has the following attributes: name, age, and address. 
#It should also have a method called get_info() that returns a string with the person's name, age, and address. 
#Then create two subclasses, Student and Teacher, that inherit from Person and add additional attributes and methods specific to each role.

from dataclasses import dataclass

@dataclass
class Person:
    name:str
    age:int
    address:int
    
person1 = Person("Agne", 24, "Klaipeda")
print(person1)

@dataclass
class Student(Person):
    grade:float

student1 = Student("Agne", 24, "Klaipeda", 9.4)
print(student1)

@dataclass
class Teacher(Person):
    years_in_school:int

