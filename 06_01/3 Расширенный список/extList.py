from overload import overload


class ExtList:
    @overload
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], (list, tuple, set)):
            self.__lst = list(args[0])
        else:
            self.__lst = list(args)

    @__init__.add
    def __init__(self) -> None:
        ...

    @__init__.add
    def __init__(self, iterable: Union[list, tuple, set]) -> None:
        ...

    @__init__.add
    def __init__(self, *args: object) -> None:
        ...


    def __len__(self):
        return len(self.__lst)

    def __iter__(self):
        return iter(self.__lst)

    def __reversed__(self):
        return ExtList(list(reversed(self.__lst)))

    def __add__(self, other):
        return ExtList(self.__lst + list(other))

    def __mul__(self, n):
        return ExtList(self.__lst * n)

    def head(self, n=0):
        if n > len(self) or n < 0:
            raise IndexError("Индекс вне диапазона")
        if n in (None, 0, 1):
            return self.__lst[0]
        return self.__lst[:n]

    def tail(self, n=0):
        if n > len(self) or n < 0:
            raise IndexError("Индекс вне диапазона")
        if n in (None, 0, 1):
            return self.__lst[1:]
        return self.__lst[-n:]

    def last(self):
        if not self.__lst:
            raise IndexError("Список пуст")
        return self.__lst[-1]

    def append(self, x):
        self.__lst.append(x)
    def clear(self):
        self.__lst.clear()
    def copy(self):
        return ExtList(self.__lst.copy())
    def count(self, x):
        return self.__lst.count(x)
    def extend(self, iterable):
        self.__lst.extend(iterable)
    def index(self, x, *args):
        return self.__lst.index(x, *args)
    def insert(self, i, x):
        self.__lst.insert(i, x)
    def pop(self, i=-1):
        return self.__lst.pop(i)
    def remove(self, x):
        self.__lst.remove(x)
    def reverse(self):
        self.__lst.reverse()
    def sort(self, key=None, reverse=False):
        self.__lst.sort(key=key, reverse=reverse)
    def __del__(self):
        self.__lst = None
