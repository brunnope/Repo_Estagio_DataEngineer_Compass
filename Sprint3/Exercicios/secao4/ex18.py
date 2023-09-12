speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}

lista = list(speed.values())

#tranformo em um set para tirar os valores duplicados e depois passo para list novamente como pede a questão
#achei melhor assim do que percorrer a lista e fazer os testes
lista = list(set(lista).intersection(lista))
print(lista)