# Duck Typing

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("I am a dog.")

class Cat(Animal):
    def speak(self):
        print("I am a cat.")

class Car:

    alive = False

    def speak(self):
        print("I am a car.")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)