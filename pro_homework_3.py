# exercise 1
class Rectangle:

    def __init__(self, length, width):
        self.length = length
        if not isinstance(length, int | float):
            raise TypeError()
        self.width = width
        if not isinstance(width, int | float):
            raise TypeError()

    def __str__(self):
        return f'length: {self.length} width: {self.width}'

    def __add__(self, other):
        tmp = self.square_rectangle() + other.square_rectangle
        return tmp

    def __mul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        return self.length * other, self.width * other

    def square_rectangle(self):
        return int(f'{self.length * self.width}')

    def __lt__(self, other):
        return self.value() < other.value()

    def value(self):
        return self.length * self.width

    def __gt__(self, other):
        return self.value() > other.value()

    def __eq__(self, other):
        return self.value() == other.value()

    def rectangle_x_n(self, n: int | float):
        if not isinstance(n, int | float):
            raise TypeError()
        return n * (int(f'{self.length  * self.width}'))


rec_1 = Rectangle(2, 3)
rec_2 = Rectangle(5, 3)
print("S1=", rec_1.square_rectangle())
print("S2=", rec_2.square_rectangle())
res = rec_1 > rec_2
print(res)
rec_3 = rec_1.square_rectangle() + rec_2.square_rectangle()
print("S3=", rec_3)


rec_4 = rec_1.rectangle_x_n(4)
print("n x = ", rec_4)

# exercise 2



