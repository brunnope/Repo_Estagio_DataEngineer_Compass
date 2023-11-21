import csv

animais = ['Elefante', 'Pinguim', 'Borboleta', 'Leão', 'Golfinho', 'Jacaré', 'Tartaruga', 'Girafa', 'Sapo', 'Canguru',
'Tubarão', 'Esquilo', 'Polvo', 'Rinoceronte', 'Águia', 'Orangotango', 'Tucano', 'Ouriço', 'Antílope', 'Camaleão']

animais.sort()

print(*animais, sep="\n")

with open('exerciciosSparkBatch/tarefa3/Animais.csv', "w", newline='', encoding='utf-8') as arq:
    escritor = csv.writer(arq)

    escritor.writerows(animais)

print(f"Arquivo Animais.csv criado com sucesso!")