def soma(texto):
    resul = 0
    nums = texto.split(',')
    for num in nums:
        resul += int(num)
    
    return resul

print(soma("1,3,4,6,10,76"))