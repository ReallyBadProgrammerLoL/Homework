class Bell:
    __obj_count = 0

    def __init__(self):
        self.__next_sound = "ding"
        type(self).__obj_count = type(self).__obj_count + 1

    def __del__(self):
        type(self).__obj_count = type(self).__obj_count - 1

    def sound(self):
        print(self.__next_sound)
        if self.__next_sound == "ding":
            self.__next_sound = "dong"
        else:
            self.__next_sound = "ding"

    @classmethod
    def get_obj_count(cls):
        return cls.__obj_count


print(Bell.get_obj_count())
obj1 = Bell()
obj2 = Bell()

print(obj1.get_obj_count())
print(Bell.get_obj_count())

obj1.__del__()

print(obj1.get_obj_count())
print(Bell.get_obj_count())

"""
1.Метод может вызвать и экземпляр класса, ибо в методе не self, а cls, который ссылается сразу на класс
2.Сколько угодно, но первым параметром всегда идёт cls
3.type принимает на вход экземпляр, а возвращает класс объекта
По сути аналог cls, но доступный вне @classMethod
"""
