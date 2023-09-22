import csv

dados = []
with open("estudantes.csv", 'r') as arquivo:
    leitor_csv = csv.reader(arquivo)
    for linha in leitor_csv:
        dados.append(linha)

estudantes = []
for aluno in dados:
    temp = []
    temp.append(aluno[0])   
    notas = sorted(aluno[1:], reverse=True, key=lambda i: int(i))
    notas = list(map(lambda i: int(i), notas))
    temp.append(notas[0:3])
    temp.append(round(sum(notas[0:3]) / 3, 2))
    estudantes.append(temp)

estudantes = sorted(estudantes)
for i in estudantes:
    print(f"Nome: {i[0]} Notas: {i[1]} Média: {i[2]}")