with open('actors.csv', 'r') as arquivo:
    dados = arquivo.readlines()
    lista_dados = []
    
    #desconsiderei a primeira coluna que é os tipos de informações e coloquei cada cada elemento de dados (linha do arquivo) como sendo uma nova lista para melhor iteração. 
    for i in dados[1:]:
        lista_dados.append(i.split(','))

soma=0
cont=0

#peguei o ultimo valor que corresponde a coluna gross e adicionei todos para soma. Utilizei um contador para calcular a media, mesmo sabendo que são 50 valores. Fiz isso pensando que caso atualizasse o arquivo, serviria de qualquer forma a resolução 
for i in lista_dados:
    soma += float(i[-1])
    cont+=1

print(f'Media: US${soma/cont:.2f} milhões')