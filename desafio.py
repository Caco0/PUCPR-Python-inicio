lista = [-10, -9, -8, -7, -6, -5, -4, -3, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
impares_negativos = []
pares_positivos = []
for i, item in enumerate(lista):
    # print(f"Indice: {i} - numero: {item}")
    if item < 0 and item % 2 != 0:
        impares_negativos.append(item)
    if item > 0 and item % 2 == 0:
        pares_positivos.append(item)
for item in impares_negativos:
    print(f"impares negativos: {item}")

for item in pares_positivos:
    print(f"pares positivos: {item}")
