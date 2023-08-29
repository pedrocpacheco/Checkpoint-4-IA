# Importando funções que facilitam o codigo
from utils import get_quantity, get_numeros


# Função que pega os valore e seus pesos
def get_valor_peso():
  quantity = get_quantity()
  
  print("Por favor informe os valores: ")
  valores = get_numeros(quantity)
  
  print("Por favor informe os pesos: ")
  pesos = get_numeros(quantity)
  
  return [valores, pesos]

# Função que multiplica os valores pelos seus pesos
def get_produtos(valores, pesos):
  produtos = []
  for i in range(len(valores)):
    valor_pesado = valores[i] * pesos[i]
    produtos.append(valor_pesado)
    
  return produtos


# Função que faz a matemática da média ponderada
def media_ponderada():
  [valores, pesos] = get_valor_peso()
  
  produtos = get_produtos(valores, pesos)
  
  total_peso = 0
  for peso in pesos:
    total_peso += peso
    
  total_produto = 0
  for produto in produtos:
    total_produto += produto
    
  result = total_produto / total_peso
  print(f"Media Ponderada: {result}")
  
# Chamando função média ponderada
media_ponderada()