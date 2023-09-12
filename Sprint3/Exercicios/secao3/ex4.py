#fiz um contador para o numero de divisões possíveis de 1 até o número atual do range. Se for apenas duas, é um primo.
for i in range(1,101):
    cont = 0
    for z in range(1,i+1):
        if i % z == 0:
            cont +=1
    if cont == 2:
        print(i)