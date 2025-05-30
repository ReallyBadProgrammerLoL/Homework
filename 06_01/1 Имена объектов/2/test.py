import test_import

class NewClass:
   pass


def new_func():
   pass

print("Имя модулей")
print(f"Имя запускаемого файла: {__name__}\nВсегда __main__!!!\n")
print(f"Имя импортируемого файла: {test_import.__name__}")


print("\nИмя созданных класса и функции: ")
print(NewClass.__name__, id(NewClass))
print(new_func.__name__, id(new_func()))



CopyClass = NewClass
copy_func = new_func
print("\nИмя копий класса и функции: ")
CopyClass.__name__ = "CopyClass"
print(CopyClass.__name__, id(CopyClass))
print(copy_func.__name__, id(copy_func()))

"""
Откуда при запуске кода из примера Podkatalog Bell появилась первая строка вывода, если в коде примера Podkatalog Bell ее нет?
Ответ: при импорте test.zip.py он интерпретируется и как следствии выводится строка

Какое имя получает файл *.py при самостоятельном запуске?
Ответ: он булет выполняться как main - как точка входа

Какое имя получает файл *.py при импорте в другой модуль?
Ответ: будет название файла без py


Какое имя получает копия класса или функции?
Ответ: Копии ссылаются на оригинал


Можно ли изменить имя класса, функции, модуля вручную?
Ответ: можно, атрибут name изменяемый

"""