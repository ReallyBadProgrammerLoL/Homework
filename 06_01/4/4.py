spi = [1,2,5,6,'h','i']
'''print(spi[6]) list index out of range '''

class DefList(list):
    def __init__(self, *args):
        super().__init__(args)
    def __getitem__(self, item=0):
        try:
            return super().__getitem__(item)
        except IndexError:
            print(f"Ошибка вы вышли за границы списка")

arg1 = DefList(1,2,4,5)
print(arg1)
print(arg1[1])
print(arg1[4])