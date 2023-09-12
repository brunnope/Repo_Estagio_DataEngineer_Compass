class Calculo:
    def __init__(self):
        self.x = None
        self.y = None
    
    def soma(x, y):
        return x + y
    
    def subtracao(x, y):
        return x-y
    
x = 4
y = 5
print(f"Somando: {x}+{y} = {Calculo.soma(x,y)}")
print(f"Subtraindo: {x}-{y} = {Calculo.subtracao(x,y)}")