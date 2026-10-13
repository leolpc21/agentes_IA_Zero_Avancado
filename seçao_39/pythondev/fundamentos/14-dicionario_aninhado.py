import pprint

filmsDict = {
    "The Matrix": {
        "year": 1999,
        "director": "Lana Wachowski, Lilly Wachowski",
        "cast": ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"],
        "genre": ["Science Fiction", "Action"],
        "rating": 8.7
    },
    "Inception": {
        "year": 2010,
        "director": "Christopher Nolan",
        "cast": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"],
        "genre": ["Science Fiction", "Action", "Thriller"],
        "rating": 8.8
    },
    "Interstellar": {
        "year": 2014,
        "director": "Christopher Nolan",
        "cast": ["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain"],
        "genre": ["Science Fiction", "Adventure", "Drama"],
        "rating": 8.6
    }
}

print(type(filmsDict)) # <class 'dict'>
pprint.pprint(filmsDict) 
""" {'Inception': {'cast': ['Leonardo DiCaprio',
                        'Joseph Gordon-Levitt',
                        'Elliot Page'],
               'director': 'Christopher Nolan',
               'genre': ['Science Fiction', 'Action', 'Thriller'],
               'rating': 8.8,
               'year': 2010},
 'Interstellar': {'cast': ['Matthew McConaughey',
                           'Anne Hathaway',
                           'Jessica Chastain'],
                  'director': 'Christopher Nolan',
                  'genre': ['Science Fiction', 'Adventure', 'Drama'],
                  'rating': 8.6,
                  'year': 2014},
 'The Matrix': {'cast': ['Keanu Reeves',
                         'Laurence Fishburne',
                         'Carrie-Anne Moss'],
                'director': 'Lana Wachowski, Lilly Wachowski',
                'genre': ['Science Fiction', 'Action'],
                'rating': 8.7,
                'year': 1999}}
                """

# Buscar uma informação específica dentro do dicionário aninhado
print(f"Diretor de Inception: {filmsDict['Inception']['director']}") # Diretor de Inception: Christopher Nolan
print(f"Ano de Interstellar: {filmsDict['Interstellar']['year']}") # Ano de Interstellar: 2014
print(f"Classificação de The Matrix: {filmsDict['The Matrix']['rating']}") # Classificação de The Matrix: 8.7

# Adicionar um novo filme ao dicionário aninhado
filmsDict["The Dark Knight"] = {
    "year": 2008,
    "director": "Christopher Nolan",
    "cast": ["Christian Bale", "Heath Ledger", "Aaron Eckhart"],
    "genre": ["Action", "Crime", "Drama"],
    "rating": 9.0
}
filmsDict["The Dark Knight"]["budget"] = 185000000
print(filmsDict["The Dark Knight"]) # {'year': 2008, 'director': 'Christopher Nolan', 'cast': ['Christian Bale', 'Heath Ledger', 'Aaron Eckhart'], 'genre': ['Action', 'Crime', 'Drama'], 'rating': 9.0, 'budget': 185000000}

# Excluir um filme do dicionário aninhado
del filmsDict["The Dark Knight"]
print(filmsDict) # {'The Matrix': {'year': 1999, 'director': 'Lana Wachowski, Lilly Wachowski', 'cast': ['Keanu Reeves', 'Laurence Fishburne', 'Carrie-Anne Moss'], 'genre': ['Science Fiction', 'Action'], 'rating': 8.7}, 'Inception': {'year': 2010, 'director': 'Christopher Nolan', 'cast': ['Leonardo DiCaprio', 'Joseph Gordon-Levitt', 'Elliot Page'], 'genre': ['Science Fiction', 'Action', 'Thriller'], 'rating': 8.8}, 'Interstellar': {'year': 2014, 'director': 'Christopher Nolan', 'cast': ['Matthew McConaughey', 'Anne Hathaway', 'Jessica Chastain'], 'genre': ['Science Fiction', 'Adventure', 'Drama'], 'rating': 8.6}}

"""
Exercício 9 - Dicionário

Escreva um programa que:
- Leia o nome de três produtos e seus respectivos preços.
- Armazene os dados em um dicionário, onde a chave é o nome do produto e o valor é o preço (float).

Imprima:
- O dicionário completo.
- O produto mais caro.
- A média dos preços.

Exemplo
Entrada:
Arroz
15.50
Feijão
8.90
Macarrão
6.75


Saída:
{'Arroz': 15.5, 'Feijão': 8.9, 'Macarrão': 6.75}
Arroz
10.38
"""

produtos = {
  "Arroz": 15.50,
  "Feijão": 8.90,
  "Macarrão": 6.75
}

print(produtos)
print(max(produtos, key=produtos.get)) # Produto mais caro: Arroz
media_precos = sum(produtos.values()) / len(produtos)
print(f"{media_precos:.2f}") # Média dos preços: 10.38 

# Explica: 
# A função `max(produtos, key=produtos.get)` retorna a chave do dicionário `produtos` que possui o maior valor associado. O argumento `key=produtos.get` faz com que a função `max` utilize os valores do dicionário para determinar qual é o maior, em vez de comparar as chaves diretamente.

# Explica .2f:
# O formato `.2f` é usado para formatar números de ponto flutuante (float) com duas casas decimais. O `f` indica que o número deve ser exibido como um número de ponto flutuante, e o `.2` especifica que queremos exatamente duas casas decimais após o ponto. Por exemplo, se a média dos preços for 10.375, o uso de `.2f` resultará em 10.38, arredondando o valor para cima. Se a média fosse 10.374, o resultado seria 10.37, arredondando para baixo. Isso é útil para exibir valores monetários de forma consistente e legível, garantindo que sempre haja duas casas decimais, mesmo que o número seja um inteiro (por exemplo, 10.00).