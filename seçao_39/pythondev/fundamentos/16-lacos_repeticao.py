# Listas
moviesList = ["Titanic", "The Godfather", "Inception", "Jurassic Park"]

# Iterando valores de uma lista

# For
for movie in moviesList:
    print(movie)

# Quando a condição é atendida, o loop é encerrado
for movie in moviesList:
    if movie == "Inception":
        break
    print(movie)

# Quando a condição for atendida, o loop vai pra próxima iteração
for movie in moviesList:
    if movie == "Inception":
        continue
    print(movie)

# Avaliação do filme

movieName = input("Digite o nome do filme: \n")
movieRating = int(input("Digite quantas avaliações deseja fazer: \n"))
total = 0

for i in range(movieRating):
    note = float(input("Digite a nota para o filme: \n"))
    total += note

if movieRating > 0:
    average = total / movieRating
else:
    average = 0

print(f"Média de avaliação do filme {movieName} é: {average:.2f}")

# While

# Iterando valores de uma lista
index = 0
while index < len(moviesList):
    print(moviesList[index])
    index += 1

# Quando a condição for atendida, o loop será encerrado
index = 0
while index < len(moviesList):
    if moviesList[index] == "Inception":
        break
    print(moviesList[index])
    index += 1

# Quando a condição for atendida, o loop vai pra proxima iteração
index = 0
while index < len(moviesList):
    if moviesList[index] == "Inception":
        index += 1
        continue
    print(moviesList[index])
    index += 1

# Avaliaçao do filme
movieName = input("Digite o nome do filme: \n")
movieRating = int(input("Digite quantas avaliações deseja fazer: \n"))
total = 0
count = 0

while count < movieRating:
    note = float(input("Digite a nota para o filme: \n"))
    total += note
    count += 1

if movieRating > 0:
    average = total / movieRating
else:
    average = 0

print(f"Média de avaliação do filme {movieName} é: {average:.2f}")
