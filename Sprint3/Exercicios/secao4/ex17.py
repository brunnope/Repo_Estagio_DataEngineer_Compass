def divLista(lista):
    quant = int (len(lista) / 3)
    lista1 = lista[:quant]
    lista2 = lista[quant:quant*2]
    lista3 = lista[quant*2:]
    return lista1,lista2,lista3

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(divLista(lista)[0], end=' ')
print(divLista(lista)[1], end=' ')
print(divLista(lista)[2])