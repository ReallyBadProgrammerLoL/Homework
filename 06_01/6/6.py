class A:
    def __str__(self):
        return "class A"

    def common(self):
        print("common_A")

    def A_method(self):
        print("Некоторый текст")

class B:
    def __str__(self):
        return "class B"

    def common(self):
        print("common_B")

    def B_method(self):
        print("Уже другой текст")

class C(A, B):
    pass

class D(B, A):
    pass

class X(C):
    pass

class Y(D):
    pass

class Z(C, D):
    pass

#экземпляры

c = C()
print('C:', c)
c.common()
"""выводит коммон и класс А, т.к. он первый в списке"""

d = D()
print('D: ', d)
d.common()
"""выводит коммон и класс В, т.к. теперь он первый в списке"""

"""вывод: структура множественного класса = св-ва класса №1 + св-ва класса №2"""

x = X()
print('X: ', x)
x.common()

"""выводит А, так как св-ва Х = св-ва С = св-ва А + св-ва Б"""

y = Y()
print('Y: ', y)
y.common()

z = Z()
print('5', z)
z.common()

"""не работает, так как С и D наследуют А и В в разном порядке. Должно быть (A+В)+(А+B), а выходит (A+B)+(B+A), нужный порядок определить не получается"""