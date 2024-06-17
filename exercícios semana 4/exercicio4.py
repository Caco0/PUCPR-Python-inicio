"""Exercício de fixação 4: Crie um programa que efetue a soma de duas 
matrizes 3x3, sabendo que a soma desse tipo de matriz é uma nova 
matriz 3x3, sendo cada elemento resultado da soma dos elementos das 
matrizes na mesma posição. Exemplo:"""

matriz1 = []
matriz2 = []
matriz_final = []
for i in range(3):
    matriz1.append([])
    matriz2.append([])
    for _ in range(3):
        matriz1[i].append(int(input(f"Digite o elemento matriz 1_")))
        matriz2[i].append(int(input(f"Digite o elemento matriz 2_")))
for i in range(3):
    matriz_final.append([])
    for j in range(3):
        matriz_final[i].append(matriz1[i][j] + matriz2[i][j])

print(f"Matriz 1:{matriz1}")
print(f"Matriz 2:{matriz2}")
print(f"Matriz final{matriz_final}")
