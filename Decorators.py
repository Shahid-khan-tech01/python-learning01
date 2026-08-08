
def add_sugar(func):
    def wrapper(*args, **kwargs):
        print("* You Added sugar in your drink🍸 *")
        print()
        func(*args, **kwargs)
    return wrapper

def add_ice(func):
    def wrapper(*args, **kwargs):
        print("* You Added ice in your drink🧊🧊 *")
        print()
        func(*args, **kwargs)
    return wrapper

def add_lemon(func):
    def wrapper(*args, **kwargs):
        print("You also Added a piece of lemon in it!🍋🍋")
        print()
        func(*args, **kwargs)
    return wrapper

@add_lemon
@add_ice
@add_sugar
def get_juice(flavor):
    print(f"Here is your {flavor} mojito, Enjoy!🍷🍷")

get_juice("blue berry")