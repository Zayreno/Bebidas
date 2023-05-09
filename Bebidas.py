class Bebida:

    fria = True

    def servir(self):
        print("A bebida foi servida")

    def beber(self):
        print("A bebida foi bebida")

class Cocacola(Bebida):
    def servir(self):
        print("A coca-cola foi servida")

class Pepsi(Bebida):
    def servir(self):
        print("A pepsi foi servida")

class Sumol(Bebida):
    def servir(self):
        print("A sumol foi servida")


cocacola = Cocacola()
pepsi = Pepsi()
sumol = Sumol()


cocacola.servir()
pepsi.servir()
sumol.servir()