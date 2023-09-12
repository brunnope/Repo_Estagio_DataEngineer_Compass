palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']
for palavra in palavras:
    palindromo = palavra[::-1]
    if palindromo == palavra:
        print(f"A palavra: {palavra} é um palíndromo")
    else:
        print(f"A palavra: {palavra} não é um palíndromo")