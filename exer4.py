# Importando funções que facilitam o codigo
from utils import get_quantity, get_numeros


# Função que calcula a soma dos quadrados diferenciais
def get_soma_quadrados(quantity):
    numeros = get_numeros(quantity)
    
    media = sum(numeros) / quantity
    
    soma_quadrados_diferencas = sum((numero - media) ** 2 for numero in numeros)
    
    return soma_quadrados_diferencas


# Função que calcula variancia amostral
def variancia_amostral():
  
    quantity = get_quantity()
    variancia = get_soma_quadrados(quantity) / (quantity - 1)
    
    print(f"Variancia Amostral: {variancia}")

# Chamando função de variancia amostral
variancia_amostral()


# Função que calcula variancia populacional
def variancia_populacional():
   
    quantity = get_quantity()
    variancia = get_soma_quadrados(quantity) / quantity  
    
    print(f"Variancia Populacional: {variancia}")

# Chamando função de variancia populacional
variancia_populacional()


# Função de desvio padrão amostral
def desvio_padrao_amostral():
  
    quantity = get_quantity()
    
    variancia = get_soma_quadrados(quantity) / (quantity - 1)
    
    desvio_padrao = variancia ** 0.5  
    
    print(f"Desvio Padrão Amostral: {desvio_padrao}")

# Chamando função de desvio padrão amostral
desvio_padrao_amostral()


# Função de desvio padrão populacional
def desvio_padrao_populacional():
  
    quantity = get_quantity()
    
    variancia = get_soma_quadrados(quantity) / quantity  
    
    desvio_padrao = variancia ** 0.5  
    
    print(f"Desvio Padrão Populacional: {desvio_padrao}")

# Chamando função de desvio padrão populacional
desvio_padrao_populacional()


# Função de incerteza de média
def incerteza_media():
  
    quantity = get_quantity()
    
    desvio_padrao_amostral = (get_soma_quadrados(quantity) / (quantity - 1)) ** 0.5
    
    incerteza = desvio_padrao_amostral / (quantity ** 0.5)
    
    print(f"Incerteza Média: {incerteza}")

# Chamando função de incerteza da média
incerteza_media()