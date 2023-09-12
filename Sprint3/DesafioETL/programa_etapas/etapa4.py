with open('actors.csv', 'r') as arquivo:
    dados = arquivo.readlines()
    lista_dados = []
    
    #desconsiderei a primeira coluna que é os tipos de informações e coloquei cada cada elemento de dados (linha do arquivo) como sendo uma nova lista para melhor iteração. 
    for i in dados[1:]:
        lista_dados.append(i.split(','))
    
filmes = {}
for i in lista_dados:
    cont=0
    for z in lista_dados:
        if i[-2] == z[-2]:
            cont += 1
    filmes[i[-2]] = cont

"""usei o lambda como uma chave de ordenação para o sorted onde utiliza o "-item[1]" para ordenar o valor em ordem decrescente(sinal de -)
e por segundo critério o nome (item[0]) utlizando como base a tupla formada em "filmes.items()". O resultado final é convertido para dicionário
"""
filmes_ordenados = dict(sorted(filmes.items(), key=lambda item: (-item[1], item[0])))
for c,v in enumerate(filmes_ordenados.items()):
    print(f"{c+1}- O filme {v[0]} aparece {v[1]} vez(es) no dataset")
