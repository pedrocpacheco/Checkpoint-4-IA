# Este arquivo é só uma outra versão do exer2, eu vi que o codigo ficou muito
# Complexo e fui tentar melhorar com a ajuda do chat gpt, e resultou nisso:

def get_valores_e_pesos():
    quantity = int(input("Digite a quantidade de itens: "))
    
    valores = []
    pesos = []

    for i in range(quantity):
        valor = int(input(f"Digite o valor {i + 1}: "))
        peso = int(input(f"Digite o peso {i + 1}: "))

        valores.append(valor)
        pesos.append(peso)

    return valores, pesos

def media_ponderada():
    valores, pesos = get_valores_e_pesos()

    total_produto = sum(valor * peso for valor, peso in zip(valores, pesos))
    total_peso = sum(pesos)

    resultado = total_produto / total_peso

    print(f"A média ponderada é: {resultado}")

media_ponderada()

# As coisas legais que aprendi fazendo isso, foi a função zip() que usa duas listas em conjunto
# Que facilita demais o processo de fazer a média, e de poder retornar mais de um valor só com a ,