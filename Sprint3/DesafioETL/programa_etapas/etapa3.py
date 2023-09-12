with open('actors.csv', 'r') as arquivo:
    dados = arquivo.readlines()
    lista_dados = []
    
    #desconsiderei a primeira coluna que é os tipos de informações e coloquei cada cada elemento de dados (linha do arquivo) como sendo uma nova lista para melhor iteração. 
    for i in dados[1:]:
        lista_dados.append(i.split(','))
    
ator = lista_dados[0][0]
quant = float(lista_dados[0][3])

#utilizei como base a resolução do exercicio anterior, usando a coluna posição 3 que seria Avarage per Movie
for i in lista_dados[1:]:
    i[3] = float(i[3])
    if i[3] > quant:
        ator = i[0]
        quant = i[3]
    
print(ator)
