frutas = ["laranja", "banana", "maçã", "pera", "abacaxi", "manga"]

# for item in frutas:
#     print(item)

# fução enumerate

pares = []
impares = []
for i, item in enumerate(frutas):
    print(f"Índice: {i} - Fruta: {item}")

print("=========================\n")
for i, item in enumerate(frutas):
    if i < 3:
        print(f"Índice: {i} - Fruta: {item}")

print("=========================\n")

for i, item in enumerate(frutas):
    if i % 2 == 0:
        pares.append(item)
    else:
        impares.append(item)
print(frutas)
for i, item in enumerate(frutas):
    print(f"Índice: {i} - Fruta: {item}\n")

print("========pares========")
for item in pares:
    print(f"Pares: {item}")

print("========Impares========")
for item in impares:
    print(f"Impares: {item}")
