with open('number.txt', 'r') as arquivo:
    numeros = arquivo.read().splitlines()

numerosInt = map(lambda i: int(i), numeros)
numerosPares = filter(lambda i: i%2==0, numerosInt)
maiores = sorted(numerosPares,reverse=True)
maiores = maiores[0:5]
print(maiores)
print(sum(maiores))