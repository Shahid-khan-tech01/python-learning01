#  MULTIPLE INHERITANCE : The class inherited from more than one parent class.
#                                C(A, B)
#  MULTI LEVEL INHERITANCE : The class inherit from a parent class which is inherited from another parent class.
#                                C(B) < - B(A) < - A

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"The {self.name} is eating")

    def sleep(self):
        print(f"The {self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"The {self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"The {self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

print()
print("**********************************")
print(f"The name of the rabbit is: {rabbit.name}")
rabbit.eat()
rabbit.sleep()
rabbit.flee()
# Rabbit can't hunt so no use of hunt()
print()
print("**********************************")
print(f"The name of the hawk is: {hawk.name}")
hawk.eat()
hawk.sleep()
hawk.hunt()
# Hawk can't flee so no use of flee()
print()
print("**********************************")
print(f"The name of the fish is: {fish.name}")
fish.eat()
fish.sleep()
fish.hunt()
fish.flee()
# Fish can do both hunting and fleeing
print()
print("**********************************")
