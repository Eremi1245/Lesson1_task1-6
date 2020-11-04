# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.
class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.i = -1

    def __add__(self, other):
        return self.a + (self.b * self.i) + other.a + (other.b * other.i)

    def __mul__(self, other):
        return self.a + (self.b * self.i) * other.a + (other.b * other.i)


com1 = ComplexNumber(5, 6)
com2 = ComplexNumber(8, 4)
print(com1 + com2)
print(com1 * com2)
