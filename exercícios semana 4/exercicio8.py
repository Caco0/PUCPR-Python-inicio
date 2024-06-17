"""Exercício de fixação 8: Crie um programa que solicite o nome de quatro 
times de futebol e simule partidas de forma que cada time jogue uma vez com os 
outros três. Na partida, deve perguntar quantos gols fez cada time e somar as 
devidas pontuações. Ao final, deve dizer quais times foram campeões, uma vez 
que pode haver empate em pontuação. Observação: vitória vale 3 pontos para o 
vencedor, empate vale 1 ponto para cada time e derrota não soma pontos"""

times = []
tabela = [0, 0, 0, 0]
for _ in range(4):
    times.append(input("Digite o nome do time: "))
for i in range(3):
    for j in range(i + 1, 4):
        print(f"Jogo:{times[i]} x {times[j]}")
        gols_i = int(input(f"Gol do time {times[i]}: "))
        gols_j = int(input(f"Gol do time {times[j]}: "))
        if gols_i > gols_j:
            tabela[i] += 3
        elif gols_i < gols_j:
            tabela[j] += 3
        else:
            tabela[i] += 1
            tabela[j] += 1
print("***Pontuação***")
for i in range(4):
    print(f"Time {times[i]}: {tabela[i]} pontos")
maior = max(tabela)
for i in range(4):
    if tabela[i] == maior:
        print(f"O time campeão é o {times[tabela.index(tabela[i])]}")
