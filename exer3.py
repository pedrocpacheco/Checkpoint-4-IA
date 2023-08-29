# Importando funções que facilitam o codigo
from utils import get_quantity, get_numeros


# Função que encontra a moda de uma lista
def moda():
  quantity = get_quantity()
  numeros = get_numeros(quantity)
  
  moda = 0
  maior_contagem = 0
  
  for numero in numeros:
    contagem = numeros.count(numero)
    if(contagem > maior_contagem):
      moda = numero 
      maior_contagem = contagem
  
  print(f"Moda: {moda}")

# Chamando função que mostra moda
moda()


# Função que encontra a mediana de uma lista
def mediana():
  quantity = get_quantity()
  numeros = get_numeros(quantity)
  
  numeros.sort()
  tamanho_lista = len(numeros)
  if(tamanho_lista % 2 == 0):
    valor1 = numeros[tamanho_lista // 2]
    valor2 = numeros[tamanho_lista // 2 - 1]
    mediana = (valor1 + valor2) / 2
    print(mediana)
  else: 
    mediana = numeros[tamanho_lista // 2]
    print(f"Mediana: {mediana}")
  
# Chamando função que mostra mediana
mediana()