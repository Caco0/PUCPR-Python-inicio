"""_Manipulando listas Acessando dados de uma lista_
"""

# Acessando dados de uma lista

# nums = [1, 4, 23, 11, 18]
# for i in range(len(nums)):
#     print(nums[i])

# nums = [1, 4, 23, 11, 8]
# for num in nums:
#     print(num)

nums = [17, 33, 23, 11, 8, 15, 9]
maior = nums[0]
menor = nums[0]
for num in nums:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f"O maior número da lista é {maior} e o menor número da lista é {menor}")
