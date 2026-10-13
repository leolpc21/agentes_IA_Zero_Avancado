filmsSet = {"Inception", "The Matrix", "Interstellar", "The Dark Knight"}

print(type(filmsSet))  # <class 'set'>

# Buscar tamanho do set

print(len(filmsSet))  # 4

# True e 1 são considerados iguais, assim como False e 0. Portanto, não é possível ter True e 1 no mesmo set, assim como False e 0.
examplesSet = {1, 2, 3, 4, 5, True, False, 0}
print(examplesSet)  # {False, 1, 2, 3, 4, 5}

# Adicionar elementos ao set
filmsSet.add("The Lord of the Rings")
print(
    filmsSet
)  # {'Inception', 'The Matrix', 'Interstellar', 'The Dark Knight', 'The Lord of the Rings'}

# Adicionar item de outro set
filmsSet2 = {"The Lion King", "The Avengers", "The Dark Knight"}
filmsSet2.update(filmsSet)
print(
    filmsSet2
)  # {'The Lion King', 'The Avengers', 'Inception', 'The Matrix', 'Interstellar', 'The Dark Knight', 'The Lord of the Rings'}

# Remover elementos do set
filmsSet.remove("Inception")
print(
    filmsSet
)  # {'The Matrix', 'Interstellar', 'The Dark Knight', 'The Lord of the Rings'}

# Remover elementos do set sem gerar erro caso o elemento não exista
filmsSet.discard(
    "Inception"
)  # Não gera erro, mesmo que "Inception" não esteja mais no set
print(
    filmsSet
)  # {'The Matrix', 'Interstellar', 'The Dark Knight', 'The Lord of the Rings'}

"""
Exercício 8 - Set

Escreva um programa que:
Leia cinco números inteiros (podendo haver repetidos).
Armazene-os em um set para eliminar duplicatas.

Imprima:
O set resultante.
A quantidade de elementos únicos.
O maior elemento do set.

Exemplo
Entrada:
4
7
4
9
7

Saída:
{9, 4, 7}
3
9
"""

numeros = {4, 7, 4, 9, 7}

print(numeros)
print(len(numeros))
print(max(numeros))
