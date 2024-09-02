# 2.  Escreva um programa Python para remover duplicatas de uma lista.

def remover_duplicatas(lista):
    return list(set(lista))

lista = [1, 2, 2, 3, 4, 4, 5]
lista_sem_duplicatas = remover_duplicatas(lista)
print(f"Lista original: {lista}")
print(f"Lista sem duplicatas: {lista_sem_duplicatas}")
