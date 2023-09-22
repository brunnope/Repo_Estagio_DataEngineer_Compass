def conta_vogais(texto):
    vogais = list(filter(lambda char: char in 'aeiou', texto.lower()))
    return len(vogais)
