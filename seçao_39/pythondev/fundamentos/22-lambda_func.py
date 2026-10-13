# Função de potência de um número
power = lambda num: num**2
print(power(5))

# Função que verifica se um número é um par
is_even = lambda x: x % 2 == 0
print(is_even(27))
print(is_even(30))

# Função que divide um número pelo outro
div_num = lambda x, y: x / y
print(div_num(9, 3))

# Função que inverte ums string
reverse_string = lambda s: s[::-1]
print(reverse_string("String"))

# Funcionalidade relacionados aos filmes
movies_list = ["Titanic", "Jurassic Park", "Inception"]
ratings = {
    "Titanic": [8.5, 9.0, 7.5],
    "Jurassic Park": [8.0, 9.5, 6.5],
    "Inception": [5, 9.5, 7.0],
}

# Função para calcular a media de avaliações de um filme
average_rating = lambda movie_name: sum(ratings[movie_name]) / len(ratings[movie_name])
print(f"Média de avaliação do filme Titanic: {average_rating('Titanic')}")

# Função que verifica se um filme está na lista
check_movie = lambda movie_name: movie_name in movies_list
print(f"Inception está na lista? {check_movie('Inception')}")

# Função para recomendar um filme com base na avaliação média
recommmed_movie = lambda movie_name: (
    f"Recomendo assistir {movie_name} com média de {average_rating(movie_name):.2}"
)
print(f"{recommmed_movie('Titanic')}")
