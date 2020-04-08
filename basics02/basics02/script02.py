class HeadsCut:
    def __init__(self, counter):
        self.counter = counter

    def raise_counter(self):
        # self.counter = self.counter + 1
        self.counter += 1


def count(arg1, arg2):
    inst1 = HeadsCut(arg1)

    while inst1.counter != arg2:
        inst1.raise_counter()
        print(inst1.counter)


count(2, 5)
