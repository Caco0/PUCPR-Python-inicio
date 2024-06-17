# imprime na tela os valores contidos na lista nums
nums = [17, 33, 8, 11, 8, 15, 9]
print(f"{nums} Lista original")
# adiciona o elemento 10 ao final da lista
nums.append(10)
print(f"{nums} adiciona o elemento 10 ao final da lista")
# extend nums com os elementos de nums2
num2 = [3, 7]
nums.extend(num2)
print(nums)
# insere o elemento 0 na posição 2 da lista
nums.insert(2, 0)
print(nums)
# remove o elemento 11 da lista
nums.remove(11)
print(nums)
# remove e retorna o elemento na posição 7 da lista
print(nums.pop(7))
print(nums)
# cria uma cópia da nums em numsCpy
numsCpy = nums.copy()
print(numsCpy)
# remove todos os elementos de nums
nums.clear()
print(nums)
# conta quantos elementos 8 existem na lista
nums = numsCpy.copy()
print(nums.count(8))
# ordena nums em ordem ascendente
nums.sort()
print(nums)
# inverte os elementos de nums
nums.reverse()
print(nums)
# ------------------função len()-----------------------------------
# retorna o tamanho da lista
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(len(nums))  # isto mostrará o valor "10"

nome = "Python"

print(len(nome))  # isto mostrará o valor "6"

# ------------------função max()-----------------------------------
# retorna o maior elemento da lista
nums = [17, 33, 8, 11, 8, 15, 9]

print(max(nums))  # isto mostrará o valor "33"

# Caso os elementos da lista sejam strings,
# a comparação é feita tomando por base a ordem alfabética.
herois = ["Zorro", "Capitão América", "Hulk", "Super-Homem"]

print(max(herois))  # isto mostrará o valor "Zorro"
