class Lampada():
    def __init__(self,estado=False):
        self.ligada = estado
    
    def liga(self):
        self.ligada = True
    
    def desliga(self):
        self.ligada = False
    
    def esta_ligada(self):
        return True if self.ligada else False

lampada1 = Lampada()
lampada1.liga()
lampada1.liga()
print(f"A lâmpada está ligada? {lampada1.esta_ligada()}")
lampada1.desliga()
print(f"A lâmpada ainda está ligada? {lampada1.esta_ligada()}")
