"""_Exercício de fixação 1: Crie um programa que solicite ao usuário seis 
números, calculando a média, e mostre uma lista com os números iguais 
ou acima da média e uma lista com os números abaixo da média._
"""

numeros = []
maiores = []
menores = []
# Solicita os numeros e calcula a média dos valores digitados
for _ in range(6):
    numeros.append(int(input("Digite um número: ")))
media = sum(numeros) / len(numeros)
for num in numeros:
    if num > media:
        maiores.append(num)
    else:
        menores.append(num)
print(f"A média dos numeros é: {media}")
print(f"Os numeros maiores que a média são {maiores}")
print(f"Os numeros menores que a média são {menores}")
