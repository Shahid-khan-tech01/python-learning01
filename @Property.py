#  @ PROPERTY
class Square:
    def __init__(self, side):
        self._side = side

    @property
    def side(self):
        return f"The side is: {self._side:.1f}cm"

    @side.setter
    def side(self, new_side):
        if new_side > 0:
            self._side = new_side
        else:
            print("Side must be positive")

    @side.deleter
    def side(self):
        del self._side
        print("Side has been deleted")


square = Square(5)

square.side = -7
print(square.side)
del square.side


