class Aviao:
    def __init__(self, modelo,velocidade_maxima,capacidade,cor="Azul"):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.cor = cor
        self.capacidade = capacidade
    
lista_objects = [Aviao("BOIENG456",1500,400), Aviao("Embraer Praetor 600",863,14), Aviao("Antonov An-2",258,12)]

for i in lista_objects:
    print(f'O avião de modelo {i.modelo} possui uma velocidade máxima de {i.velocidade_maxima}, capacidade para {i.capacidade} passageiros e é da cor {i.cor}')