filmsList = ["Inception", "The Matrix", "Interstellar", "The Dark Knight"]

# 1 - Tamanho da lista
print(f"1: {len(filmsList)}")  # 4

# 2 - Retornar o index da lista pelo nome do elemento
print(f"2: {filmsList.index('The Matrix')}")  # 1

# 3 - Adicionar um elemento ao final da lista
filmsList.append("Tenet")
print(
    f"3: {filmsList}"
)  # ['Inception', 'The Matrix', 'Interstellar', 'The Dark Knight', 'Tenet']

# 4 - Adicionar um elemento em uma posição específica
filmsList.insert(1, "The Godfather")
print(
    f"4: {filmsList}"
)  # ['Inception', 'The Godfather', 'The Matrix', 'Interstellar', 'The Dark Knight', 'Tenet']

# 5 - Ordernar a lista em ordem alfabética
filmsList.sort()
print(
    f"5: {filmsList}"
)  # ['Inception', 'Interstellar', 'Tenet', 'The Dark Knight', 'The Godfather', 'The Matrix']

# 6 - Copiar os itens de uma lista para outra
filmsList2 = filmsList.copy()
print(
    f"6: {filmsList2}"
)  # ['Inception', 'Interstellar', 'Tenet', 'The Dark Knight', 'The Godfather', 'The Matrix']

# 7 - Remover um elemento da lista
filmsList2.remove("The Dark Knight")
print(
    f"7: {filmsList2}"
)  # ['Inception', 'Interstellar', 'Tenet', 'The Godfather', 'The Matrix']

# 8 - Remover um elemento em uma posição específica
filmsList.pop(0)
print(
    f"8: {filmsList}"
)  # ['Interstellar', 'Tenet', 'The Dark Knight', 'The Godfather', 'The Matrix']

# 9 - Limpar todos os elementos da lista
filmsList.clear()
print(f"9: {filmsList}")  # []

"""
Exercício 6 - Listas

Escreva um programa que:
- Leia 3 números inteiros.
- Armazene esses números em uma lista.

Imprima:
A lista completa.
O primeiro elemento da lista.
A soma de todos os elementos da lista.

Exemplo
Entrada:
5
7
2

Saída:
[5, 7, 2]
5
14
"""

numeros = [5, 7, 2]

print(numeros)  # [5, 7, 2]
print(numeros[0])  # 5
print(sum(numeros))  # 14
