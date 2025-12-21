# Inheritance

```python
"""
Inheritance in Python
This file demonstrates inheritance and its types.
"""

# Single Inheritance

class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

car = Car()
car.start()
car.drive()


# Multiple Inheritance

class Father:
    def skill1(self):
        print("Gardening")

class Mother:
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    pass

child = Child()
child.skill1()
child.skill2()


# Multilevel Inheritance

class Grandparent:
    def house(self):
        print("Has a house")

class Parent(Grandparent):
    def car(self):
        print("Has a car")

class Child2(Parent):
    def bike(self):
        print("Has a bike")

c = Child2()
c.house()
c.car()
c.bike()


# Hierarchical Inheritance

class Animal:
    def eat(self):
        print("Eating food")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

dog = Dog()
cat = Cat()

dog.eat()
dog.sound()

cat.eat()
cat.sound()


# Method Overriding and super()

class Person:
    def __init__(self, name):
        self.name = name
        print("Person constructor called")

class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no
        print("Student constructor called")

s = Student("Kahkashan", 14)
