class Word(str):
    def __new__(cls, word):
        return super().__new__(cls, word)

    def count_glas(self):
        vowels = "aeiouyAEIOUYаеёиоуыэюяАЕЁИОУЫЭЮЯ"
        return sum(1 for char in self if char in vowels)

    def __lt__(self, other):
        return self.count_glas() < other.count_glas()

    def __le__(self, other):
        return self.count_glas() <= other.count_glas()

    def __eq__(self, other):
        return self.count_glas() == other.count_glas()

    def __ne__(self, other):
        return self.count_glas() != other.count_glas()

    def __gt__(self, other):
        return self.count_glas() > other.count_glas()

    def __ge__(self, other):
        return self.count_glas() >= other.count_glas()

words = [ Word("овошь"), Word("машинка"), Word("гайка"), Word("армия"), Word("поход")]
for word in words:
        print(f"{word} ({word.count_glas()} слогов)")
print(sorted(words))