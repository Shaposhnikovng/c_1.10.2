class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def squere_rectangle(self):
        return self.a * self.b

rec_1 = Rectangle(2, 3)
print("Размеры прямоугольника, см")
print("==========================")
print(f"Ширина: {rec_1.get_a()}\nДлина: {rec_1.get_b()}\n")
print("Площадь прямоугольника, см")
print("==========================")
print(f"Площадь: {rec_1.squere_rectangle()}")