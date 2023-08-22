def get_quantity():
    quantity = int(input("Digite a quantidade de itens: "))
    return quantity

def get_numeros(quantity):
    numeros = []
    for i in range(quantity):
        valor = int(input(f"Digite o valor {i + 1}: "))
        numeros.append(valor)
    return numeros

def get_total(op, numeros):
    total = 0
    if op == "+":
        for valor in numeros: 
            total += valor
    if op == "*":
        for valor in numeros:
            total *= valor