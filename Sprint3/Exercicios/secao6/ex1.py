class Passaro:
    def __init__(self):
        self.som = None
        self.tipo = None

    def voar(self):
        return "Voando..."

    def emitirSom(self):
        return self.som

class Pato(Passaro):
    def __init__(self):
        super().__init__()
        self.tipo = "Pato"
        self.som = "Quack Quack"

class Pardal(Passaro):
    def __init__(self):
        super().__init__()
        self.tipo = "Pardal"
        self.som = "Piu Piu"  

pato = Pato()
pardal = Pardal()

print(pato.tipo)
print(pato.voar())
print(f"{pato.tipo} emitindo som...")
print(pato.emitirSom())
print(pardal.tipo)
print(pardal.voar())
print(f"{pardal.tipo} emitindo som...")
print(pardal.emitirSom())