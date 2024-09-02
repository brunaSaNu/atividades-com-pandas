#3. Faça três programas que utilizem módulos nativos do Python (três módulos deverão ser utilizados, no mínimo, isto é, ao menos um módulo diferente em cada um dos programas).
import math
import random
from datetime import datetime


#Programa 1 - importei o math para fazer calculo da hipotenusa
def calcular_hipotenusa(cateto1, cateto2):
    return math.sqrt(cateto1**2 + cateto2**2)

c1 = float(input("Digite o valor do primeiro cateto: "))
c2 = float(input("Digite o valor do segundo cateto: "))
print(f"A hipotenusa é: {calcular_hipotenusa(c1, c2)}")



#Programa 2 - importei o random para gerar o número de um relatório
def gerar_numero_aleatorio(inicio, fim):
    return random.randint(inicio, fim)
print(f"Número aleatório entre 1 e 100: {gerar_numero_aleatorio(1, 100)}")



#Programa 3 - importei o datetime para dar a hora atual
def obter_data_atual():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print(f"A data e hora atual é: {obter_data_atual()}")
