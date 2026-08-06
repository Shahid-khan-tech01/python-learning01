#   Inheritance : It allows a class to inherit attributes and methods from another class.

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"The {self.name} is eating the food")

    def sleep(self):
        print(f"The {self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("BARK!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Mouse(Animal):
    def speak(self):
        print("SQUEEK!")

dog = Dog("Scooby")
cat = Cat("Persian")
mouse = Mouse("Mickey")

print("***********************")
dog.eat()
cat.eat()
mouse.eat()
print()
print("***********************")
print()
dog.sleep()
cat.sleep()
mouse.sleep()
print()
print("************************")
dog.speak()
cat.speak()
mouse.speak()