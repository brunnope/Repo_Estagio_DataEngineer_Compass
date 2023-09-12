with open('actors.csv', 'r') as arquivo:
    dados = arquivo.readlines()
    lista_dados = []
    
    #desconsiderei a primeira coluna que é os tipos de informações e coloquei cada cada elemento de dados (linha do arquivo) como sendo uma nova lista para melhor iteração. 
    for i in dados[1:]:
        lista_dados.append(i.split(','))
    
atores = {}
#cria um dict com o nome e a receita como valor, já em ordem decrescente como está no arquivo
for i in lista_dados:
    atores[i[0]] = i[1]

for c,v in atores.items():
    print(f"{c} - {v}")

