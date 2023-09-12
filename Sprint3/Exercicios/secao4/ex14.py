def teste(*tupla, **dic):
    for i in tupla:
        print(i)
    for z in dic.values():
        print(z)

teste(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)