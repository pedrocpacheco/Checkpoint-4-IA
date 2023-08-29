# Importando funções que facilitam o codigo
from utils import get_quantity, get_numeros, get_total


# Função que calcula média aritemetica
def aritmetica():
    quantity = get_quantity()
    numeros = get_numeros(quantity)
    total = get_total("+", numeros)
    result = total / quantity
    print(f"Média Aritmetica: {result}")

# Rodando função aritimetica
aritmetica()


# Função que calcula média geometrica
def geometrica():
    quantity = get_quantity()
    numeros = get_numeros(quantity)
    total = get_total("*", numeros)
    result = total ** 1/quantity
    print(f"Média Geométrica: {result}")

# Rodando função geometrica
geometrica()


# Função que calcula média harmônica
def harmonica():
    quantity = get_quantity()
    numeros = get_numeros(quantity)
    for i in range(len(numeros)):
        if numeros[i] == 0:
            numeros[i] = 0
        else:
            numeros[i] = 1 / numeros[i]
    total = get_total("+", numeros)
    result = quantity / total
    print(f"Média Harmônica: {result}")

# Rodando função geometrica
harmonica()