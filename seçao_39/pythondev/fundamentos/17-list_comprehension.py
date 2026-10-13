# Listando valores de 0 a 10 que sejam menores que 4
listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)

moviesList = ["Titanic", "The Godfather", "Inception", "Jurassic Park"]

# Filmes que possuem a letra 'e' no titulo
moviesWithE = [movie for movie in moviesList if "e" in movie.lower()]
print(moviesWithE)

# Filmes que eu assisti
moviesWatched = [movie for movie in moviesList if movie != "Jurassic Park"]
print(moviesWatched)

# Encontrando um filme pelo nome
while True:
    searchName = input(
        "Digite o nome do filme para buscar na lista (ou sair para encerrar): \n"
    )
    if searchName.lower() == "sair":
        print("Programa encerrado")
        break

    foundMovies = [movie for movie in moviesList if searchName.lower() in movie.lower()]
    if foundMovies:
        print(f"Filme(s) encontrado(s) com o nome: {searchName}:")
        for foundMovie in foundMovies:
            print(foundMovie)
    else:
        print(f"Nenhum filme foi encontrado com o nome {searchName}. Tente novamente!")
