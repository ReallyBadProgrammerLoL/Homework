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



def test_bell():
    bell = Bell()

    assert bell._Bell__next_sound == "ding", "Ошибка 1"

    bell.sound()
    assert bell._Bell__next_sound == "dong", "Ошибка Podkatalog"

    bell.sound()
    assert bell._Bell__next_sound == "ding", "Ошибка 3"

    print("Все тесты прошли успешно!")

if __name__ == "__main__":
    objBell = Bell()
    #print(Bell._Bell__next_sound)
    print(objBell._Bell__next_sound)
    print(Bell.get_obj_count())
    obj1 = Bell()
    obj2 = Bell()
    print(obj1.get_obj_count())
    print(Bell.get_obj_count())
