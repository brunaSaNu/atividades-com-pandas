# 1 Faça um programa que utilize duas funções definidas por você.

def dia(nome):
    return f"Bom dia, {nome}!"

def soma(a, b):
    return a + b

# Programa principal
nome_usuario = input("Digite seu nome: ")
print(dia(nome_usuario))

numero1 = int(input("Digite o primeiro número que deseja somar: "))
numero2 = int(input("Digite o segundo número que deseja somar: "))
print(f"A soma de {numero1} e {numero2} é: {soma(numero1, numero2)}")
