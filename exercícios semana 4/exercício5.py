identidade = []
tamanho = int(input("Qual é o tamanho da matriz-identidade desejada? "))
for i in range(tamanho):
    identidade.append([])
    for j in range(tamanho):
        if i == j:
            identidade[i].append(1)
        else:
            identidade[i].append(0)
for linha in identidade:
    print(linha)
