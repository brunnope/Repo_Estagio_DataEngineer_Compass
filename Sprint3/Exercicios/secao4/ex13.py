def my_map(list, f):
    lista = []
    for i in list:
        lista.append(f(i))
    return lista

def potencia2(num):
    return num ** 2

lbase = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_map(lbase,potencia2))