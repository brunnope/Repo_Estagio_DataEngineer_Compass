with open('arquivo_texto.txt', 'r') as arquivo:
    palavras = arquivo.readlines()
    for i in palavras:
        print(i, end='')