"""Exercício de fixação 3: Crie um programa que leia as temperaturas médias de 
cada mês do ano e as armazene em uma lista; use outro vetor para guardar e 
exibir, quando necessário, o nome dos meses do ano; calcule a média anual de 
temperatura e informe quais meses ficaram acima da média anual."""

meses = [
    "janeiro",
    "fevereiro",
    "março",
    "abril",
    "maio",
    "junho",
    "julho",
    "agosto",
    "setembro",
    "outubro",
    "novembro",
    "dezembro",
]
temperaturas = []
media_anual = 0
acima_media = []
for i in range(12):
    temperaturas.append(
        float(
            input(
                f"""
Digite a temperatura média do mês de {meses[i]}: """
            )
        )
    )
media_anual = sum(temperaturas) / 12
print(f"A média anual de temperatura é de {media_anual:.2f} graus celcius")
for i in range(12):
    if temperaturas[i] > media_anual:
        print(f"{meses[i]}: {temperaturas[i]:.1f} graus")
