"""_Exemplo de aplicação 9: Em uma competição de saltos ornamentais, 
são obtidas dos jurados sete notas, sendo eliminadas a maior e a menor. 
A nota final do salto é feita pela soma das demais notas. Crie um 
programa que receba as notas dos juízes, remova a maior e menor nota e 
some as demais, fazendo uso de métodos de listas e funções built in._
"""

notas = []

for _ in range(7):
    nota = float(input("Entre com uma das notas: "))
    notas.append(nota)

menor = min(notas)
if notas.count(menor) == 1:
    notas.remove(menor)
else:
    indice = -1  # Percorre toda a lista
    for i in range(len(notas)):  #
        if notas[i] == menor:  #
            indice = i  #
            break  #
    notas.pop(indice)  # retorna o menor numero da lista e o remove

maior = max(notas)
if notas.count(maior) == 1:
    notas.remove(maior)
else:
    indice = -1  # Percorre toda a lista
    for i in range(len(notas)):
        if notas[i] == maior:
            indice = i
            break
    notas.pop(indice)
soma = sum(notas)
print(f"A nota final é: {soma:.1f}")
