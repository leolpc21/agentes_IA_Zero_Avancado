
filmInception = {
    "title": "Inception",
    "director": "Christopher Nolan",
    "year": 2010,
    "cast": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"],
    "genre": ["Science Fiction", "Action", "Thriller"],
    "rating": 8.8
}

print(type(filmInception)) # <class 'dict'>

# Recuperar um elemento do dicionário
print(filmInception["title"]) # Inception
print(filmInception.get("director")) # Christopher Nolan

# Buscar apenas as chaves do dicionário
print(filmInception.keys()) # dict_keys(['title', 'director', 'year', 'cast', 'genre', 'rating'])

# Buscar apenas os valores do dicionário
print(filmInception.values()) # dict_values(['Inception', 'Christopher Nolan', 2010, ['Leonardo DiCaprio', 'Joseph Gordon-Levitt', 'Elliot Page'], ['Science Fiction', 'Action', 'Thriller'], 8.8])

# Buscar apenas os itens do dicionário
print(filmInception.items()) # dict_items([('title', 'Inception'), ('director', 'Christopher Nolan'), ('year', 2010), ('cast', ['Leonardo DiCaprio', 'Joseph Gordon-Levitt', 'Elliot Page']), ('genre', ['Science Fiction', 'Action', 'Thriller']), ('rating', 8.8)])

# Adicionar itens ao dicionário
filmInception["budget"] = 160000000
print(filmInception) # {'title': 'Inception', 'director': 'Christopher Nolan', 'year': 2010, 'cast': ['Leonardo DiCaprio', 'Joseph Gordon-Levitt', 'Elliot Page'], 'genre': ['Science Fiction', 'Action', 'Thriller'], 'rating': 8.8, 'budget': 160000000}

# Atualizar itens do dicionário
filmInception.update({"rating": 9.0})
print(filmInception) # {'title': 'Inception', 'director': 'Christopher Nolan', 'year': 2010, 'cast': ['Leonardo DiCaprio', 'Joseph Gordon-Levitt', 'Elliot Page'], 'genre': ['Science Fiction', 'Action', 'Thriller'], 'rating': 9.0, 'budget': 160000000}

# Remover itens do dicionário
filmInception.pop("budget")
print(filmInception) # {'title': 'Inception', 'director': 'Christopher Nolan', 'year': 2010, 'cast': ['Leonardo DiCaprio', 'Joseph Gordon-Levitt', 'Elliot Page'], 'genre': ['Science Fiction', 'Action', 'Thriller'], 'rating': 9.0}

# Remover o último item do dicionário
filmInception.popitem()
print(filmInception) # {'title': 'Inception', 'director': 'Christopher Nolan', 'year': 2010, 'cast': ['Leonardo DiCaprio', 'Joseph Gordon-Levitt', 'Elliot Page'], 'genre': ['Science Fiction', 'Action', 'Thriller']}  