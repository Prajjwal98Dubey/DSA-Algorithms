# There are basically four properties of OOPs 
# 1.Inheritance 2.Encapsulation 3.Abstraction 4.Polymorphism

# class Car:
#     def __init__(self,name,brand,color,price):
#         self.name=name
#         self.brand = brand
#         self.color = color
#         self.price = price
#     def __repr__(self):
#         return f"Name: {self.name},Brand: {self.brand},Color: {self.color},Price:{self.price}"  
    
# Inheritance:- it means a child class inherits the properties or the characteristics of the parent class.
# Polymorphism: we can use some method to function in a different way in a class.
    
# class Sedan(Car):
#     def __init__(self,name,brand,color,price,power):
#         super().__init__(name,brand,color,price)  # accessing the propeties of the parent class.
#         self.power = power
#     # the repr in the parent class is different and here it is different which means we have modified our __repr__ method, this concept is known as "Polymorphism".
#     def __repr__(self):
#         return f"Name: {self.name},Brand: {self.brand},Color: {self.color},Price:{self.price} power:{self.power}" 
    
# sedan1 = Sedan("Maybach","Mercedes","Black","1.2")

#Abstraction:-Python does not have the direct implementation of abstraction or it does not support the abstraction directly we use it with the following way the way in which the code is written below.

# In abstraction it is mandatory that the all the methods of the superclass must be implemented in the subclass if the subclass is inherting from that superclass.

from abc import ABC , abstractmethod
class Car(ABC):
    def __init__(self,name,brand,color,price):
        self.name=name
        self.brand = brand
        self.color = color
        self.price = price
    @abstractmethod
    def __repr__(self):
        return f"Name: {self.name},Brand: {self.brand},Color: {self.color},Price:{self.price}"
    @abstractmethod
    def sample(self):
        print("This is for testing for the parent class.")

class Sedan(Car):
    def __init__(self,name,brand,color,price,power):
        super().__init__(name,brand,color,price)
        self.power = power
    def __repr__(self):
        return f"Name: {self.name},Brand: {self.brand},Color: {self.color},Price:{self.price} power:{self.power}" 
    def sample(self):
        print("This is for testing in the child class.")

sedan1 = Sedan("Maybach","Mercedes","Black","1.2","6000")
print(sedan1)
sedan1.sample()

# Encapsultion :- hiding the details or the implementation of a function from the client,it can be implemented with the help of access modifiers (public,private,protected)