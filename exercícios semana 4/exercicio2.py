"""
Exercício de fixação 2: Crie um programa que solicite ao usuário duas listas 
com cinco elementos cada e, como resultado, crie uma terceira lista que 
intercale os elementos das anteriores.
"""

lista1 = []
lista2 = []
lista_final = []
for _ in range(5):
    lista1.append(input("Digite um elemento para a lista 1: "))
    lista2.append(input("Digite um elemento para a lista 2: "))

for i in range(5):
    lista_final.append(lista1[i])
    lista_final.append(lista2[i])

print(f"Lista final com valores intercalados: {lista_final}")
