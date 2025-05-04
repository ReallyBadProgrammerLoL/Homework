class Bell:
    def __init__(self):
        self.__next_sound = "ding"

    def sound(self):
        print(self.__next_sound)
        if self.__next_sound == "ding":
            self.__next_sound = "dong"
        else:
            self.__next_sound = "ding"

def test_bell():
    bell = Bell()

    assert bell._Bell__next_sound == "ding", "Ошибка 1"

    bell.sound()
    assert bell._Bell__next_sound == "dong", "Ошибка 2"

    bell.sound()
    assert bell._Bell__next_sound == "ding", "Ошибка 3"

    print("Все тесты прошли успешно!")

if __name__ == "__main__":
    objBell = Bell()
    #print(Bell._Bell__next_sound)
    print(objBell._Bell__next_sound)
    test_bell()