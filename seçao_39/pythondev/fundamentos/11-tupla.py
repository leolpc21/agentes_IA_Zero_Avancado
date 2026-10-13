filmsTupla = ("Inception", "The Matrix", "Interstellar", "The Dark Knight")
print(type(filmsTupla)) # <class 'tuple'>

# Buscar os dois primeiros elementos da tupla
print(filmsTupla[0:2]) # ('Inception', 'The Matrix')

# Buscar o ultimo item da tupla
print(filmsTupla[-1]) # 'The Dark Knight'

# Buscar filmes até uma determinada posição
print(filmsTupla[:3]) # ('Inception', 'The Matrix', 'Interstellar')

# Buscar filmes a partir de uma determinada posição
print(filmsTupla[2:]) # ('Interstellar', 'The Dark Knight')

# Recuperar o índice de um elemento da tupla
print(f"O índice do filme 'The Matrix' é: {filmsTupla.index('The Matrix')}") # 1

"""
Exercício 7 - Tupla

Escreva um programa que:
- Crie uma tupla com os nomes de três cidades lidas pelo usuário.

Imprima:
A tupla completa.
O último elemento da tupla.
A quantidade de elementos da tupla.

Exemplo
Entrada:
Recife
Salvador
Fortaleza

Saída:
('Recife', 'Salvador', 'Fortaleza')
Fortaleza
3
"""

cidades = ("Recife","Salvador","Fortaleza")

print(cidades)
print(cidades[-1])
print(len(cidades))