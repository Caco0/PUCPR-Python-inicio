nomes = []
while True:
    nome = input("Digite um nome (ou 'sair' para finalizar): ")
    if nome == "sair" or nome == "Sair":
        break
    sobrenome = input("Digite o sobrenome: ")
    nome_completo = [nome, sobrenome]
    nomes.append(nome_completo)

for nome in nomes:
    print(f"{nome[0]} {nome[1]}")
