m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(m[1][1])  # isto mostrará o número inteiro "5"


m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
soma = 0
for i in range(3):
    for j in range(3):
        soma += m[i][j]
print(f"A soma dos elementos da matriz m é igual a {soma}")
