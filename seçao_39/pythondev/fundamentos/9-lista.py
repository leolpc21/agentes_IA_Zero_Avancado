# Trabalhando com listas em Python
# Uma lista é uma coleção de elementos que podem ser de diferentes tipos de dados, como números, strings, booleanos, entre outros. As listas são mutáveis, o que significa que podemos

name = "Top Gun: Maverick"
year_launch = 2023
note_movie = 8.3
planIncluded = False

filme = [name, year_launch, note_movie, planIncluded]
print(filme) # ['Top Gun: Maverick', 2023, 8.3, False]
print(type(filme)) # <class 'list'>

filmsList = ["Inception", "The Matrix", "Interstellar", "The Dark Knight"]

# 1 - Buscar os dois primeiros elementos da lista
print(filmsList[0:2]) # ['Inception', 'The Matrix']

# 2 - Buscar os dois últimos elementos da lista
print(filmsList[-2:]) # ['Interstellar', 'The Dark Knight']

# 3 - Buscar um elemento específico da lista
print(filmsList[1]) # 'The Matrix'

# 4 - Buscar um elemento de uma posição em diante
print(filmsList[1:3]) # ['The Matrix', 'Interstellar']
