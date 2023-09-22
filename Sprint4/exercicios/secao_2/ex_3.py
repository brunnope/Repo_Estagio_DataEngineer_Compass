from functools import reduce
def calcula_saldo(lancamentos) -> float:
    debito = map(lambda v: v[0], filter(lambda v: v[1]=='D',lancamentos))
    credito = sum(map(lambda v: v[0],filter(lambda v: v[1]=='C',lancamentos)))

    saldoFinal = reduce(lambda x,y: x-y, debito, credito)
    return float(saldoFinal)



lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')]

print(calcula_saldo(lancamentos))