# Importando funções que facilitam o codigo
from utils import get_quantity, get_numeros, get_total

# Função que calcula média aritemetica
def aritmetica():
    quantity = get_quantity()
    numeros = get_numeros(quantity)
    total = get_total("+", numeros)
    result = total / quantity
    print(result)

# Rodando função aritimetica
aritmetica()

# Função que calcula média geometrica
def geometrica():
    quantity = get_quantity()
    numeros = get_numeros(quantity)
    total = get_total("*", numeros)
    result = total ** 1/quantity
    print(result)

geometrica()