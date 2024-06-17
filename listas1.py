pares = []
impares = []

for i in range(10):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(
    f"""
Numeros pares: {pares}...
Numeros impares: {impares}...
"""
)
