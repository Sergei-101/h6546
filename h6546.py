# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
# Создайте класс Матрица. Добавьте методы для: - вывода на печать,
# сравнения,
# сложения,
# *умножения матриц

import time

class MyStr(str):
    """Add class to str"""
    def __new__(cls, value, avtor):
        """Add copy class to str"""
        instance = super().__new__(cls, value)
        instance.avtor = avtor
        instance.time = time.time()
        return instance

    def __str__(self):
        """printout for user"""
        return f"Представления для пользователя {self.avtor} время {self.time}"

    def __repr__(self):
        """printout for programmer"""
        return f"Представления для программиста {self.avtor} время {self.time}"

a = MyStr("Name", avtor="Bob")
print(repr(a))
print(a)


class Rectangle:
    """Calculating the perimeter and area of rectangles"""

    def __init__(self, width, length):
        """Added the name parameter."""
        self.width = width
        self.length = length

    def __str__(self):
        """printout for user"""
        return f"Прямоугольник: Ширина{self.width}, Длинна {self.length}, Периметр {self.perimetr()}, Площадь {self.area()}"

    def __repr__(self):
        """printout for programmer"""
        return f"Прямоугольник: Ширина{self.width}, Длинна {self.length}, Периметр {self.perimetr()}, Площадь {self.area()}"

    def area(self):
        """counts the area"""
        return self.width * self.length

    def perimetr(self):
        """counts the perimetr"""
        return 2 * (self.width + self.length)

    def __add__(self, other):
        """rectangle addition operation"""
        summary_perimetr = self.perimetr() + other.perimetr()
        width_rectangle_c = self.width
        length_rectangle_c = summary_perimetr / 2 - width_rectangle_c
        return Rectangle(width_rectangle_c, length_rectangle_c)

    def __sub__(self, other):
        """rectangle subtraction operation"""
        summary_perimetr = abs(self.perimetr() - other.perimetr())
        width_rectangle_c = min(self.width, other.width, self.length, other.length)
        length_rectangle_c = summary_perimetr / 2 - width_rectangle_c
        return Rectangle(width_rectangle_c, length_rectangle_c)

    def __eq__(self, other):
        """comparison of rectangles"""
        return self.area() == other.area()

    def __ne__(self, other):
        """comparison of rectangles"""
        return self.area() != other.area()

    def __lt__(self, other):
        """comparison of rectangles"""
        return self.area() < other.area()

    def __le__(self, other):
        """comparison of rectangles"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """comparison of rectangles"""
        return self.area() > other.area()

    def __qe__(self, other):
        """comparison of rectangles"""
        return self.area() >= other.area()

rectangle_a = Rectangle(2, 3)
rectangle_b = Rectangle(5, 10)
print(rectangle_a.perimetr())
print(rectangle_b.perimetr())
rectangle_c = rectangle_a + rectangle_b
rectangle_d = rectangle_a - rectangle_b
print(rectangle_c.perimetr(), rectangle_c.width, rectangle_c.length)
print(rectangle_d.perimetr(), rectangle_c.width, rectangle_c.length)
print(rectangle_a == rectangle_b)



class Matrix:
    """"creating matrices"""

    def __init__(self, data):
        """Added the name parameter."""
        self.data = data

    def __str__(self):
        """printout for user"""
        return '\n'.join([' '.join(map(str, row)) for row in self.data])
    def __repr__(self):
        """printout for programmer"""
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def __add__(self, other):
        """matrix addition operation"""
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Матрицы должны быть одного размера для сложения.")

        result_data = []
        for i in range(len(self.data)):
            row = [self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))]
            result_data.append(row)

        return Matrix(result_data)

    def sum_matrix(self):
        """The sum of the numbers in the matrix"""
        return sum([j for i in self.data for j in i])

    def __eq__(self, other):
        """comparison of Matrix"""
        return self.sum_matrix() == other.sum_matrix()

    def __ne__(self, other):
        """comparison of Matrix"""
        return self.sum_matrix() != other.sum_matrix()

    def __lt__(self, other):
        """comparison of Matrix"""
        return self.sum_matrix() < other.sum_matrix()

    def __le__(self, other):
        """comparison of Matrix"""
        return self.sum_matrix() <= other.sum_matrix()

    def __gt__(self, other):
        """comparison of Matrix"""
        return self.sum_matrix() > other.sum_matrix()

    def __qe__(self, other):
        """comparison of Matrix"""
        return self.sum_matrix() >= other.sum_matrix()




test_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
test_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

print(test_1, test_2)
print(test_1 + test_2)
print(test_1.__add__(test_2))
print(test_1 > test_2)
print(test_1 < test_2)
print(test_1 == test_2)