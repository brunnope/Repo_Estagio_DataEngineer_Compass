with open('actors.csv', 'r') as arquivo:
    dados = arquivo.readlines()
    lista_dados = []
    
    #desconsiderei a primeira coluna que é os tipos de informações e coloquei cada cada elemento de dados (linha do arquivo) como sendo uma nova lista para melhor iteração. 
    for i in dados[1:]:
        lista_dados.append(i.split(','))

#setei bases de comparação baseando no nome(indice 0) e quantidade de filmes(indice 2) da matriz
ator = lista_dados[0][0]
quant = int(lista_dados[0][2])

#percorri toda a matriz, tranformei para int cada valor e fiz a comparação se a quantidade atual era maior que a base
for i in lista_dados[1:]:
    i[2] = int(i[2])
    if i[2] > quant:
        ator = i[0]
        quant = i[2]

print(f"{ator}: {quant} filmes")
