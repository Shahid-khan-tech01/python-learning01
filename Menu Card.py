# Menu Card - Concession Stand Program

menu = {
    "biryani": 120.00,
    "noodles": 90.00,
    "meat": 70.00,
    "rice": 50.00,
    "dal": 20.00,
    "chicken masala": 420.00,
    "chicken kabab": 340.00,
    "ghee Rice": 125.00,
    "carrot Halwa": 70.00,
    "pizza": 70.00
}

cart = []
total = 0

print("------------ MENU ------------")

for key, value in menu.items():
    print(f"{key:20}: ${value:.2f}")

print("-----------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("----- YOUR ORDER -----")

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Your total is: ${total:.2f}")