# MAGIC METHODS

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
# String
    def __str__(self):
        return f"{self.title} by {self.author}"
# EQUALS
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
# LESS THAN
    def __lt__(self, other):
        return self.pages < other.pages
# GREATER THAN
    def __gt__(self, other):
        return self.pages > other.pages
# ADDITION
    def __add__(self, other):
        return Book(self.title + other.title, self.author + other.author, self.pages + other.pages)
# SUBTRACTION
    def __sub__(self, other):
        return Book(self.pages - other.pages, self.pages - other.pages, self.pages - other.pages)



b1 = Book("The Travels of Ibn Battuta", "Ibn Battuta", 325)
b2= Book("The Road to Mecca", "Muhammad Asad", 375)
b3 = Book("In the Shade of the Qur'an", "Sayyid Qutb", 6000)


print(b1)
print(b2)
print(b3)
print(b1 == b2 or b2 == b3 or b3 == b1)
print(b1 < b2 or b2 < b3 or b3 < b1)
print(b1 > b2 or b2 > b3 or b3 > b1)
print(b1  +  b2 and b2 + b3 and b3 + b1)
print(b1 - b2 and b2 - b3 and b3 - b1)