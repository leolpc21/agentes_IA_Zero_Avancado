# Concatenação de Strings

name = input("Digite o nome do filme: \n")
year_launch = int(input("Digite o ano de lançamento do filme: \n"))
note_movie = float(input("Digite a nota do filme: \n"))

# Alteranativa 1 - Utilizando vírgula
print("O nome do filme é:", name, "!")

# Alteranativa 2 - Utilizando o operador de concatenação (+)
print("O ano de lançamento do filme é: " + str(year_launch) + "!")

# Alteranativa 3 - Utilizando f-string
print(f"A nota do filme é: {note_movie}!")

# Unico Print
print(f"\nO nome do filme é: {name}!\nO ano de lançamento do filme é: {year_launch}!\nA nota do filme é: {note_movie}!")

"""
Exercício 3 - Concatenando Valores
Escreva um programa que leia o nome de uma pessoa usando input() e imprima a mensagem:

"Olá, <nome>!"

(com ponto de exclamação no final e quebra de linha no final).
"""

nome = input("Digite um nome:")

print(f"Olá, {nome}!")