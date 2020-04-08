class Pierwsza:
    def foo (self):
        print ("Jestem nadrzędna!")

class Druga(Pierwsza):
    def truth(self):
        print ("Jestem w klasie nadrzędnej")

class Liar(Pierwsza):
    def lie(self):
        print ("Jestem nadrzędna")


inst1 = Pierwsza()
inst2 = Pierwsza()
inst3 = Druga()
inst4 = Druga()
inst5 = Liar()
inst6 = Liar()

inst1.foo()
inst3.truth()
inst5.lie()