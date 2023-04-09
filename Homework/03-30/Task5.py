#Create a class named Animal that has the following attributes: name and species. 
#It should also have a method called speak() that returns a string with the animal's sound.

class Animal:
    def __init__(self, name:str, species:str) -> None:
        self.name = name
        self.species = species

    def speak(self):
        return "meow"