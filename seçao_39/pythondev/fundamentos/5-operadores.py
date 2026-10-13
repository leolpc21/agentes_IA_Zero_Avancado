num1 = int(input("Digite o primeiro número: \n"))
num2 = int(input("Digite o segundo número: \n"))

#Aritmeticos
sum = num1 + num2 #soma
sub = num1 - num2 #subtração
mult = num1 * num2 #multiplicação
div = num1 / num2 #divisão

print(f"A soma dos números é: {sum}")
print(f"A subtração dos números é: {sub}")
print(f"A multiplicação dos números é: {mult}")
print(f"A divisão dos números é: {div}")

mod = num1 % num2 #modulo
print(f"O resto da divisão é: {mod}")

exp = num1 ** num2 #exponenciação
print(f"O resultado da exponenciação é: {exp}")

# Comparação

bigger = num1 > num2 #maior que
print(f"O primeiro número é maior que o segundo? {bigger}")

smaller = num1 < num2 #menor que
print(f"O primeiro número é menor que o segundo? {smaller}")

equal = num1 == num2 #igual a
print(f"O primeiro número é igual ao segundo? {equal}")

not_equal = num1 != num2 #diferente de
print(f"O primeiro número é diferente do segundo? {not_equal}")

greater_equal = num1 >= num2 #maior ou igual a
print(f"O primeiro número é maior ou igual ao segundo? {greater_equal}")

less_equal = num1 <= num2 #menor ou igual a
print(f"O primeiro número é menor ou igual ao segundo? {less_equal}")

# Atribuição

num1 += num2 #num1 = num1 + num2
num1 -= num2 #num1 = num1 - num2
num1 *= num2 #num1 = num1 * num2
num1 /= num2 #num1 = num1 / num2

"""
Exercício 4 - Operadores
Escreva um programa que leia dois números inteiros e imprima:

- A soma dos dois números
- O produto dos dois números - (produto é o resultado da multiplicação)
- Cada resultado deve ser exibido em uma linha separada.

Exemplo
Entrada:
3
5

Saída:
8
15
"""

num_1 = int(input("Digite o primeiro número: \n"))
num_2 = int(input("Digite o segundo número: \n"))

sum = num_1 + num_2
product = num_1 * num_2

print(f"A soma dos números é: {sum}")
print(f"O produto dos números é: {product}")