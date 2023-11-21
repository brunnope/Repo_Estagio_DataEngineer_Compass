import random
import names

random.seed(40)
qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

aux=[]

for i in range(0, qtd_nomes_unicos):

    aux.append(names.get_full_name())


print(f"Gerando {qtd_nomes_aleatorios} nomes aleatórios")

dados=[]

for i in range(0,qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

with open("exerciciosSparkBatch/tarefa3/nomes_aleatorios.txt", "w", newline='', encoding='utf-8') as arq:
    
    for nome in dados:
        arq.write(nome + "\n")

print(f"Arquivo criado com sucesso!")