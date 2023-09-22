def maiores_que_media(conteudo):
    media = sum([i for i in conteudo.values()]) / len(conteudo.values())
    prods = list(filter(lambda i: i[1]>media, conteudo.items()))
    prods = sorted(prods, key= lambda x: x[1])
    return prods


conteudo = {
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}

print(maiores_que_media(conteudo))