class ExtList:
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], (list, tuple, set)):
            self.__lst = list(args[0])
        else:
            self.__lst = list(args)

    def __len__(self):
        return len(self.__lst)


    def __reversed__(self):
       return ExtList(list(reversed(self.__lst)))

    def __iter__(self):
         return iter(self.__lst)

    def head(self, n=0):
        if n > self.__len__() or n < 0:
            raise IndexError("Индекс вне диапазона")
        if n is None or n == 0 or n == 1 :
            return self.__lst[0]
        return self.__lst[:n]

    def tail(self, n=0):
        if n > self.__len__() or n < 0:
            raise IndexError("Индекс вне диапазона")
        if n is None or n == 0 or n == 1:
            return self.__lst[1:]
        return self.__lst[-n:]
