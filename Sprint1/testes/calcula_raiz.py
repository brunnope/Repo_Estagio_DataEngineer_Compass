import func

num = int(input("Digite um número: "))
raiz = num **(1/2)

print(f"A raiz de {num} é {raiz:.0f}!")
print(f"A soma de {num} com 10 é {func.Soma(num,10)}!")
print(f"O dobro de {num} é {func.Dobro(num)}!")
