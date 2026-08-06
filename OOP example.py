# Objects & Class in Python  ==>
# Object = A 'Bundle' of related attribute(variables) and Methods(functions).
# Class = (Blueprint) Used to design the structure and layout of an object.

# Creating __init__ which is the constructor used for initialization


class Car:
    def __init__(self, name, price, color, year):
        self.name = name
        self.price = price
        self.color = color
        self.year = year

    def drive(self):
        print(f"You drive the {self.color} {self.name}")

    def stop(self):
        print(f"You stop the {self.color} {self.name}")

    def describe(self):
        print(f"{self.name} {self.color} {self.price} {self.year}\n")


car1 = Car("Mahindra Thar", "17.60 lakhs","Black", 2023)
car2 = Car("Tata Nexon", "15.50 lakhs","Green", 2022)
car3 = Car("Fortuner", "51.44 lakhs","Red", 2021)

print("**********************************")
print()
car1.drive()
car1.stop()
car1.describe()
print()
print("**********************************")
print()
car2.drive()
car2.stop()
car2.describe()
print()
print("**********************************")
print()
car3.drive()
car3.stop()
car3.describe()
print()
print("**********************************")