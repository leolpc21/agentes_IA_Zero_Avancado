# Pythonflix

snack_case = "top_gun_maverick"
kebab_case = "top-gun-maverick"
camel_case = "topGunMaverick"
pascal_case = "TopGunMaverick"

name = "Top Gun: Maverick"
year_launch = 2023
note_movie = 8.3
planIncluded = False

# Para saber qual é o tipo de dado de uma variável, podemos utilizar a função type().

print(type(name)) # <class 'str'> string
print(type(year_launch)) # <class 'int'> integer
print(type(note_movie)) # <class 'float'> float
print(type(planIncluded)) # <class 'bool'> boolean

"""
Exercício 2 - Tipos de Dados
Escreva um programa que imprima na tela, cada um em uma linha, um número inteiro, um número decimal (float) e um texto (string).

Formato esperado da saída:
42
3.14
Python
"""

idade = 42
valor = 3.14
nome = "Python"

print(idade)
print(valor)
print(nome)