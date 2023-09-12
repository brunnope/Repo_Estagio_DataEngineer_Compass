from datetime import datetime
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print(datetime.now().year + (100-idade))